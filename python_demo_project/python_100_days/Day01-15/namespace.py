x = 123
z=x
print(globals())

globals()['y'] = 'hello world'
print(y)

print('y type:',type(y))
y = __import__("string")
print('new y type:',type(y))

print('y value:',y.digits)