import sys,weakref

class User(object):
    pass

def callback(r):
    print("weakref object:",r)
    print("target object dead")

a = User()
#创建a的弱引用对象
r = weakref.ref(a,callback)
#弱引用不会导致该对象的引用计数增加
print(hex(id(r)),hex(id(a)))
print(r() is a)
print(sys.getrefcount(a))

#原对象被回收时弱引用会调用回调函数并同时被回收，所以简单的循环引用可以用弱引用来打破
del a
print(r() is None)