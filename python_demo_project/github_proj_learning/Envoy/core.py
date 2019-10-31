import os
import sys
import shlex #shell + lexical analyzer,可以用这个库来解析用户需要再子进程中执行的命令
import signal   #处理linux内核信号的标准库
import subprocess #实现子进程的标准库，envoy会对其进行封装
import threading#多线程标准库，
import traceback#追溯异常标准库

__version__ = '0.0.3'
__license__ = 'MIT'
__author__ = 'Kenneth Reitz'


def _terminate_process(process):
    if sys.platform == 'win32':
        import ctypes
        PROCESS_TERMINATE = 1
        handle = ctypes.windll.kernel32.OpenProcess(PROCESS_TERMINATE, False, process.pid)
        ctypes.windll.kernel32.TerminateProcess(handle, -1)
        ctypes.windll.kernel32.CloseHandle(handle)
    else:
        os.kill(process.pid, signal.SIGTERM)


def _kill_process(process):
    if sys.platform == 'win32':
        _terminate_process(process)
    else:
        os.kill(process.pid, signal.SIGKILL)


def _is_alive(thread):
    if hasattr(thread, "is_alive"):
        return thread.is_alive()
    else:
        return thread.isAlive()


class Command(object):
    def __init__(self, cmd):
        self.cmd = cmd
        self.process = None
        self.out = None
        self.err = None
        self.returncode = None
        self.data = None
        self.exc = None

    def run(self, data, timeout, kill_timeout, env, cwd):
        self.data = data
        #对环境变量的处理,把os.environ转化为dict
        environ = dict(os.environ)
        #更新，利用短路求值方式避免入参env非空，env和environ中有同名环境变量的话以env中的为主
        environ.update(env or {})

        #嵌套target函数，定义收到一个shell指令时需要做什么
        def target():

            try:
                #创建一个子进程，并执行self.cmd的shell指令
                self.process = subprocess.Popen(self.cmd,
                    universal_newlines=True,
                    shell=False,
                    env=environ,
                    stdin=subprocess.PIPE,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    bufsize=0,
                    cwd=cwd,
                )

                if sys.version_info[0] >= 3:
                    #将self.data通过pipe传给正在shell中执行的程序，并返回标准输出和标准错误
                    self.out, self.err = self.process.communicate(
                        input = bytes(self.data, "UTF-8") if self.data else None
                    )
                else:
                    self.out, self.err = self.process.communicate(self.data)
            except Exception as exc:
                #整个target函数执行过程中，任何错误都会保存在self.exc中
                self.exc = exc

        #创建一个线程将target处理函数作为入参，
        thread = threading.Thread(target=target)
        #开始执行target函数
        thread.start()
        #处理上层传下来的超时限制，此时当前主进程会阻塞，直到target中创建的子进程任务完成
        #或者超时
        thread.join(timeout)

        #target函数中创建的子进程可能抛出异常
        if self.exc:
            raise self.exc
        #当前创建的线程可能因为超时而执行到当前代码，判断当前线程是正常退出还是超时运行
        if _is_alive(thread) :
            #如果超时，关闭子进程
            _terminate_process(self.process)
            #等待线程超时终止
            thread.join(kill_timeout)
            if _is_alive(thread):
                #线程还活着，终止
                _kill_process(self.process)
                thread.join()
        self.returncode = self.process.returncode
        return self.out, self.err


class ConnectedCommand(object):
    def __init__(self,
        process=None,
        std_in=None,
        std_out=None,
        std_err=None):

        self._process = process
        self.std_in = std_in
        self.std_out = std_out
        self.std_err = std_out
        self._status_code = None

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.kill()

    @property
    def status_code(self):
        """The status code of the process.
        If the code is None, assume that it's still running.
        """
        return self._status_code

    @property
    def pid(self):
        """The process' PID."""
        return self._process.pid

    def kill(self):
        """Kills the process."""
        return self._process.kill()

    def expect(self, bytes, stream=None):
        """Block until given bytes appear in the stream."""
        if stream is None:
            stream = self.std_out

    def send(self, str, end='\n'):
        """Sends a line to std_in."""
        return self._process.stdin.write(str+end)

    def block(self):
        """Blocks until command finishes. Returns Response instance."""
        self._status_code = self._process.wait()


#是Command类实例调用run()方法后的执行结果信息
class Response(object):
    """A command's response"""

    def __init__(self, process=None):
        super(Response, self).__init__()

        self._process = process
        self.command = None
        self.std_err = None
        self.std_out = None
        self.status_code = None
        self.history = []


    def __repr__(self):
        if len(self.command):
            return '<Response [{0}]>'.format(self.command[0])
        else:
            return '<Response>'

#接收字符串入参，然后解析为一个个的命令
def expand_args(command):
    """Parses command strings and returns a Popen-ready list."""

    # Prepare arguments.
    if isinstance(command, (str)):
        #构造一个词法分析器，以'|'分割，类似于split("|")
        splitter = shlex.shlex(command.encode('utf-8'))
        splitter.whitespace = '|'
        splitter.whitespace_split = True
        command = []

        while True:
            token = splitter.get_token()
            if token:
                command.append(token)
            else:
                break

        command = list(map(shlex.split, command))
    print("split command:",command)
    return command

#执行一个shell指令并返回response
def run(command, data=None, timeout=None, kill_timeout=None, env=None, cwd=None):
    """Executes a given commmand and returns Response.
    Blocks until process is complete, or timeout is reached.
    """
    #解析指令返回command的list
    command = expand_args(command)

    history = []
    for c in command:

        #模拟管道pipe，传入上个程序的标准输出最大10KB到这里
        if len(history):
            # due to broken pipe problems pass only first 10 KiB
            data = history[-1].std_out[0:10*1024]

        #在子进程中执行指令
        cmd = Command(c)
        try:
            out, err = cmd.run(data, timeout, kill_timeout, env, cwd)
            status_code = cmd.returncode
        except OSError as e:
            out, err = '', u"\n".join([e.strerror, traceback.format_exc()])
            status_code = 127
        #执行指令得到输出，将相关的输出保存在history list中缓存
        r = Response(process=cmd)

        r.command = c
        r.std_out = out
        r.std_err = err
        r.status_code = status_code

        history.append(r)

    #返回最后一个pipe之后命令的输出和详细情况
    r = history.pop()
    r.history = history

    return r


def connect(command, data=None, env=None, cwd=None):
    """Spawns a new process from the given command."""

    # TODO: support piped commands
    command_str = expand_args(command).pop()
    environ = dict(os.environ)
    environ.update(env or {})

    process = subprocess.Popen(command_str,
        universal_newlines=True,
        shell=False,
        env=environ,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        bufsize=0,
        cwd=cwd,
    )

    return ConnectedCommand(process=process)

if __name__ == "__main__":
    expand_args('cat inFile | sort | uniq')