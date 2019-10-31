from math import hypot

class Vector:
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y

    #通过这个方法得到一个对象的字符串表示形式
    #__str__是在print函数打印一个对象或者str()函数里面调用
    #如果一个对象没有__str__函数又需要调用它的时候，解释器会用__repr__作为替代
    def __repr__(self):
        return "Vector(%r %r)" %(self.x,self.y)
    
    def __abs__(self):
        return hypot(self.x,self.y)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self,other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x,y)
    
    def __mul__(self,scalar):
        return Vector(self.x*scalar,self.y*scalar)

    