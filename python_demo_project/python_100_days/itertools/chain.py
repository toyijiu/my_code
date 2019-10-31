from itertools import *
#chain连接多个迭代器
it = chain(range(3),"abc")
print(list(it))
#combinations返回指定长度的顺序组合序列
it = combinations("abcd",2)
print(list(it))
#如果想额外返回同一元素的组合
it = combinations_with_replacement("abcd",2)
print(list(it))
#compress按条件过滤迭代器元素
it = compress("abcde",[1,0,1,1,0])
print(list(it))
#count从起点开始无限循环下去
for x in count(10,step=2):
    print(x)
    if x > 17:
        break
#cycle迭代结束从头来过
for i,x in enumerate(cycle("abc")):
    print(x)
    if i>7:
        break