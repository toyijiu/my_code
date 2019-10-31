
import copy
#不可变类型number tuple string
print("对于不可变类型Number String Tuple，浅拷贝只是地址指向，不会开辟新的内存空间")
num1 = 17
num2 = copy.copy(num1)
print('num1,num2 address:',hex(id(num1)),hex(id(num2)))

str1 = 'hello'
str2 = copy.copy(str2)
print('str1,str2 address:',hex(id(str1)),hex(id(str2)))

tup1 = (18,'jack')
tup2 = copy.copy(tup1)
print('tup1,tup2 address:',hex(id(tup1)),hex(id(tup2)))

print("="*20)
print("对于可变类型 List、Dictionary、Set，浅复制会开辟新的空间地址(仅仅是最顶层开辟了新的空间)，进行浅拷贝")

list1 = [1,2]
list2 = copy.copy(list1)
print('list1,list2 address:',hex(id(list1)),hex(id(list2)))
print('list1[0],list2[0] address:',hex(id(list1[0])),hex(id(list2[0])))





