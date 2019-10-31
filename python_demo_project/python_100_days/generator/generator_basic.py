class Data(object):
    def __init__(self,*args):
        self._data = list(args)
    
    def __iter__(self):
        #编译器会把yield返回的值打包成Generator对象，实现了迭代器的generator对象
        for x in self._data:
            yield x
        
d = Data(1,2,3)
print(d.__iter__())

for x in d:
    print(x)