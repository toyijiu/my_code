#!/usr/bin/env python
#()表示必选参数 []表示可选参数 <>表示位置参数
"""Usage:
  pip-diff (--fresh | --stale) <reqfile1> <reqfile2> [--exclude <package>...]
  pip-diff (-h | --help)
Options:
  -h --help     Show this screen.
  --fresh       List newly added packages.
  --stale       List removed packages.
"""
import os
from docopt import docopt
from pip.req import parse_requirements
from pip.index import PackageFinder
from pip._vendor.requests import session
#参考总结：https://chybeta.github.io/2018/10/12/pip-pop-%E6%BA%90%E7%A0%81%E9%98%85%E8%AF%BB/
#起一个session对象引用，session就是包含http相关的attribute
"""
'headers', 'cookies', 'auth', 'proxies', 'hooks', 'params', 'verify',
'cert', 'prefetch', 'adapters', 'stream', 'trust_env','max_redirects'
"""
requests = session()

class Requirements(object):
    def __init__(self,reqfile=None):
        #这个是python2和python3的一个区别，
        # Python 3 可以使用直接使用 super().xxx 代替 super(Class, self).xxx
        super(Requirements,self).__init__()
        self.path = reqfile
        self.requirements = []
        if reqfile:
            self.load(reqfile)
        #和__str__类似，repr是面向程序员的，print或者直接调用对象都会调用
        #__str__面向用户，print会打印，直接调用对象则是显示相关属性和内存地址
        def __repr__(self):
            return '<Requirements \'{}\'>'.format(self.path)

        def load(self,reqfile):
            #如果文件路径不存在，报错
            if not os.path.exists(reqfile):
                raise ValueError("the given requirements file does not exist.")
            #PackageFinder一个例子：https://www.programcreek.com/python/example/84759/pip.index.PackageFinder
            """
            关于PackageFinder和parse_requirements，可以去查询pip的github源码：
            https://github.com/pypa/pip
            parse_requirements的定义:https://github.com/pypa/pip/blob/master/src/pip/_internal/req/req_file.py
            parse_requirements会逐行读取文件内容
            """
            finder = PackageFinder([],[],session=requests)
            for requirment in parse_requirements(reqfile,finder=finder,session=request):
                if requirment.req:
                    if not getattr(requirment.req,"name",None):
                        requirment.req.name = requirment.req.project_name
                    self.requirements.append(requirment.req)
        
        #比较两个file的不同点，解析出新增的和去除的
        def diff(self,requirements,ignore_versions=False,excludes=None):
            r1 = self
            r2 = requirements
            results = {'fresh':[],'stale':[]}

            #产生第一个文件r1的fresh package
            other_reqs = (
                [r.name for r in r1.requirements]
                if ignore_versions else r1.requirements
            )

            #遍历r2的每一行，找到没在r1中的
            for req in r2.requirements:
                r = req.name if ignore_versions else req
                if r not in other_reqs and r not in excludes:
                    results['fresh'].append(req)
            
            #产生第二个文件r2的stale package
            other_reqs = (
                [r.name for r in r2.requirements]
                if ignore_versions else r2.requirements
            )

            #比较找到stale的例子
            for req in r1.requirements:
                r = req.name if ignore_versions else req
                if r not in other_reqs and r not in excludes:
                    results['stale'].append[req]
            
            return results
            

def diff(r1,r2,include_fresh=False,include_stale=False,excludes=None):
    include_versions = True if include_stale else False
    excludes = excludes if len(excludes) else []

    try:
        r1 = Requirements(r1)
        r2 = Requirements(r2)
    except ValueError:
        print("There was a problem loading the given requirements files")
        exit(os.EX_NOINPUT)
        
    results = r1.diff(r2,ignore_versions=True,excludes=excludes)
    if include_fresh:
        if include_versions:
            for line in results['fresh']:
                print(line.name)
        else:
            for line in results['fresh']:
                print(line)
    
    if include_stale:
        if include_versions:
            for line in results['stale']:
                print(line.name)
        else:
            for line in results['stale']:
                print(line)
    
def main():
    #获取对应的命令行参数，返回一个Dict对象给args
    args = docopt(__doc__,version='pip-diff')
    #通过kwargs解析对应的变量
    #fresh和stale参数是来产生两个文件之间的增减记录
    kwargs = {
        'r1':args['<reqfile1>'],
        'r2':args['<reqfile2>'],
        'include_fresh':args['--fresh'],
        'include_stale':args['--stale'],
        'excludes':args['<package>']
    }

    diff(**kwargs)

if __name__ == "__main__":
    main()