import gc

class User(object):
    def __del__(self):
        print(hex(id(self))," will be deleted")

#关掉gc
gc.disable()

#python GC将要回收的对象分成3级代龄,GENO管理新加入的年轻对象，GEN1管理上次回收后存活的对象
#GEN2管理声明周期很长的对象，每次GENO对象数量超过阈值时会引发GC
a = User()
del a
print(gc.get_threshold())
print(gc.get_count())