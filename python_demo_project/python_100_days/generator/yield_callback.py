#用yield来实现异步回调调用
#常用的callback异步回调
def framework(logic,callback):
    s = logic()
    print("[FX]logic is:",s)
    print("[FX]do something..")
    callback("async:" + s)

def logic():
    s = "mylogic"
    return s

def callback(s):
    print(s)

framework(logic,callback)

#用yield
def framework(logic):
    try:
        it = logic()
        s = next(it)
        print("logic:",s)
        it.send("async:"+s)
    except StopIteration:
        pass

def logic2():
    s = "mylogic"
    r = yield s
    print(r) 

framework(logic2)
