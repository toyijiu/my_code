#python模块是运行期对象，模块对应同名源码文件，为成员提供全局名字空间
"""
__name__:模块名
__file__:模块完整文件名
__dict__:模块globals名字空间
"""
#动态创建模块对象
import sys,types

m = types.ModuleType("sample","sample module.")
print(m)
print(m.__dict__)
print("sample" in sys.modules)
def test():
    print("test")

m.test = test
m.test()