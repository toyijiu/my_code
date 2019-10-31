class Person(object):
    __slots__ = ('_name','_age','_gender')

    def __init__(self,name,age):
        self._name = name
        self._age = age
    
    #getter
    @property
    def name(self):
        return self._name
    
    @property
    def age(self):
        return self._age
    
    #setter
    @age.setter
    def age(self,age):
        self._age = age

    def play(self):
        if self._age >= 16:
            print("%s is playing card" %(self._name))
        else:
            print("%s is playing game" %(self._name))


def main():
    person = Person("jack",20)
    person.play()
    person.age = 12
    person.play()
    person._gender = "man"

if __name__ == "__main__":
    main()