from functools import partial

def test(a,b,c):
    print(a,b,c)

f = partial(test,b=2,c=3)
f(1)

f = partial(test,4,c=6)
f(5)