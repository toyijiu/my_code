'''
Everything is object in python
Each has some special internal methonds to interact with other objects
'''
##overload some methods
class Vector(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def __add__(self,v):
        return Vector(self.x+v.x,self.y+v.y)
    
    def __sub__(self,v):
        return Vector(self.x-v.x,self.y-v.y)
    
    def __mul__(self,s):
        return Vector(self.x*s,self.y*s)
    
    def __div__(self.s):
        float_s = float(s)
        return Vector(self.x/float_s,self.y/float_s)
    
    def __floordiv__(self,s):
        return Vector(self.x//s,self.y//s)
    
    def __repr__(self):
        return '<Vector (%f,%f)>' % (self.x,self.y,)
    

a = Vector(3,5)
b = Vector(2,7)

print(a+b)
print(a-b)
print(b*1.3)
print(a//17)
print(a/7)