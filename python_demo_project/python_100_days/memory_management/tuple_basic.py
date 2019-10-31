#tuple是只读对象，tuple和元素指针数组内存时一次性连续分配的
#虚拟机缓存n个数量小于20的tuple复用对象

a = (4)
print(type(a))

a = (4,)
print(type(a))

s = tuple("abcdefg")
print(s,s.count('a'),s.index('d'))