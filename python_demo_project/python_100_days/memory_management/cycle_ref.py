#循环引用的demo例子
import gc,weakref,sys

class User(object):
    #一旦有了__del__ gc对循环引用也没有办法了
    def __del__(self):
        pass
    

def callback(r):
    print(r," is dead")

gc.disable()

a = User()
wa = weakref.ref(a,callable)
b = User()
wb = weakref.ref(b,callback)
print('weak ref address:',hex(id(wa)),hex(id(wb)))
#形成循环引用
a.b = b
b.a = a
print('count:',sys.getrefcount(a),sys.getrefcount(b))

del a
del b

#计数机制对循环引用无效
print('weak ref',wa(),wb())

gc.set_debug(gc.DEBUG_STATS | gc.DEBUG_LEAK)
gc.enable()
print('is gc enable:',gc.isenabled())

#手动触发gc
gc.collect()
