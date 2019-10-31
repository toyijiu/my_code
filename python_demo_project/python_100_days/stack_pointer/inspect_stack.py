import inspect

def controller():
    context = "hello world!"
    model()
def model():
    print(get_context())
def get_context():
    for f in inspect.stack():
        context = f[0].f_locals.get("context")
        if context:
            return context


controller()
#sys._current_frames返回所有线程的当前堆栈帧对象，虚拟机会预先缓存200个堆栈帧复用，以获得
#更好的执行性能
