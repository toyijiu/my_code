def test():
    x = [1,2]
    print(hex(id(x)))

    def a():
        x.append(3)
        print(hex(id(x)))
    
    def b():
        x.append(4)
        print(hex(id(x)))
    
    return a,b

#返回函数a和b时只是返回函数的对象，没有调用他们，所以不会创建堆栈帧，每次调用
#返回的都是新建对象
a,b = test()
a()
b()
print(a.__closure__)
print(b.__closure__)
#test在创建a和b时，将他们引用的外部对象x添加到func_closure 列表中，让x的引用计数增加了就算test
#堆栈帧没有了，x对象也不会被回收
