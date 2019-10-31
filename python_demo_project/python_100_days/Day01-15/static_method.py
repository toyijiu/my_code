from math import sqrt

class Triangle(object):
    
    __slots__ = ('_a','_b','_c')

    def __init__(self,a,b,c):
        self._a = a
        self._b = b
        self._c = c
    
    @staticmethod
    def is_valid(self):
        return a+b>c and a+c>b and b+c>a

    def get_perimeter(self):
        return self._a + self._b + self._c
    
    def get_size(self):
        half = self.perimeter() / 2
        return sqrt(half * (half - self._a) *
                    (half - self._b) * (half - self._c))