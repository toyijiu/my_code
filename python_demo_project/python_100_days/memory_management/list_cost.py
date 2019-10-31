#list使用realloc()来调整指针数组内存大小，存在潜在的性能隐患
#
import itertools,gc,timeit

gc.disable()
def test():
    return len([0 for i in range(10000)]) #先创建list，然后不断append

def test2():
    return len(list(itertools.repeat(0,10000)))#按照迭代器创建列表对象，一次分配内存

print(timeit.timeit(stmt=test,number=100))
print(timeit.timeit(stmt=test2,number=100))

#可以直接用数组array来代替list，和list存储对象指针不同，array直接内嵌数据，接收创建的内存开销
#而且提升读写效率
