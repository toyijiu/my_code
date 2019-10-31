from collections import namedtuple

City = namedtuple('City','name country population coordinates')

tokyo = City('Tokyo','JP',36.933,(35.689722,139.691667))

if __name__ == "__main__":
    print(tokyo,tokyo.name,tokyo.population)
    print('fields:',tokyo._fields)