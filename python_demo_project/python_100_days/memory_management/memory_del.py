#python采用引用计数法来管理对象的内存回收，对于循环引用的场景就只能靠GC了
class User(object):
    def __del__(self):
        print("will be dead")
    
a = User()
b = a
print(a is b)
import sys
count = sys.getrefcount(a)
print("a count:",count)

del a
count = sys.getrefcount(b)
print("b count:",count)

del b