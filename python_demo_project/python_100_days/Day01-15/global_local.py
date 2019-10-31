import sys



def test(x):
    y = x + 100
    print(locals())
    #此时globals和locals指向不同的名字空间
    print(globals() is locals())
    #获取当前堆栈帧
    frame = sys._getframe(0)
    print(locals() is frame.f_locals)
    print(globals() is frame.f_globals)


if __name__ == "__main__":
    print("compare over the function:",globals() is locals())
    test(123)