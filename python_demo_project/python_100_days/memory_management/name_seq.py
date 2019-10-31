__builtins__.b = "builtins"

g = "globals"

def enclose():
    e = "enclosing"
    def test():
        l = "locals"
        print(l)
        print(e)
        print(g)
        print(b)
        
    return test

t = enclose()
t()