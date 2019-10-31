import sys
a = 15
b = a
print(a is b)
print(sys.getrefcount(a))

a = 25777
b = a
print(a is b)
print(sys.getrefcount(a))