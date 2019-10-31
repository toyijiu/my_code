import sys

x = 0x1234
print('x size:',sys.getsizeof(x))

#读取头部的引用计数
print('x ref count:',sys.getrefcount(x))

y = x

print('x ref count:',sys.getrefcount(x))

del y 
print('x ref count:',sys.getrefcount(x))