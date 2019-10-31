def test(a,*args,**kwargs):
    s = "hello,world!"
    print(locals())

test(1,"a","b",x=10,y="hi")

#函数内部使用赋值语句，总是在locals名字空间中新建一个对象关联，赋值是指名字指向新的对象
#名字查找顺序：locals->enclosing function -> globals ->__builtins__