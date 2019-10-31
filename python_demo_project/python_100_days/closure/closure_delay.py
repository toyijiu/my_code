#闭包的延迟获取状态
def test():
    for i in range(3):
        def a():
            print(i)
        yield a

#test只是返回对象，没有执行，完成for循环时i已经是2了，所以执行函数时i都是2
a,b,c = test()
a()
b()
c()