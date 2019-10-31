#当整数的范围超过int上限时(一般int的位数和当前的系统位数保持一致),会自动转换成long
#long的位数是动态调整的变长变量
import sys

#python2 是maxint，python3是maxsize
#python2超过int范围后会自动转long ，python3没有上限限制，还是int
a = sys.maxsize
print(type(a),a)

b = a*10000
print(type(b),b)