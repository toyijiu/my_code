def str_test():
    str1 = "hello, world!"
    print(len(str1))
    print(str1.capitalize())
    print(str1.upper())
    print(str1.find('or'))
    print(str1.find('shit'))
    #和find类似，但是找不到会返回异常，find是返回-1
    print(str1.index('or'))
    print(str1.startswith('hello'))
    print(str1.endswith('world!'))
    #将字符串以指定的宽度居中并在两侧填充指定字符
    print(str1.center(20,"*"))
    print(str1.rjust(30,"*"))
    print(str1.ljust(30,"*"))

    str2 = "abc123456"
    print(str2[2])
    print(str2[2:5])
    print(str2[2:])
    print(str2[2::2])
    print(str2[::-1])
    print(str2[-3::-1])
    print(str2.isdigit())
    print(str2.isalpha())
    #字符串是否是由数字和字符组成
    print(str2.isalnum())

def list_test():
    list1 = [1,3,5,7,100]
    print(list1)
    list2 = ['hello']*5
    print(list2)
    print(len(list1))
    print(list1[-1])
    list1.append(2000)
    list1.insert(1,233)
    print(list1)
    if 233 in list1:
        list1.remove(233)
        print(list1)
    list1.clear()
    print(list1)

def slice_test():
    list1 = [1,2,3,4]
    list1 += [5,6,7]
    for i in list1:
        print(i,end='')
    list2 = list1[1:]
    print(hex(id(list1[0])),hex(id(list2[0])),hex(id(list1[1])))
if __name__ == "__main__":
    a = 1
    b = 1
    c = 1
    print(hex(id(a)),hex(id(b)),hex(id(c)))
    d = 257 
    e = 257
    f = 257
    print(hex(id(d)),hex(id(e)),hex(id(f)))
    slice_test()
