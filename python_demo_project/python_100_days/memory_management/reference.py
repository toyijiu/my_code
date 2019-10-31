a = object()
b = a
print(b is a)
print(hex(id(a)),hex(id(b)))

def test(x):
    print(hex(id(x)))

test(a)