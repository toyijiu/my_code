
class Data(object):
    def __init__(self,*args):
        self._data = list(args)
    
    def __iter__(self):
        return DataIter(self)
    
    def add(self,x):
        self._data.append(x)
    
    def data(self):
        #返回迭代器对象而不是self._data list，可以避免对象状态被外部修改，tuple会浪费内存空间
        return iter(self._data)

#自己重写iterator实现
class DataIter(object):
    def __init__(self,data):
        self._index = 0
        self._data = data._data
    
    def __next__(self):
        if self._index >= len(self._data):
            raise StopIteration()
        d = self._data(self._index)
        self._index += 1
        return d

d = Data()
d.add(1)
d.add(2)
d.add(3)

for x in d.data():
    print(x)

k = Data(4,5,6)
it = iter(k)
next(it)
next(it)
next(it)


