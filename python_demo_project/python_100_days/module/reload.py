#当模块源文件发生变更时，reload可以重新导入模块，新建模块对象依旧使用原内存地址
import sys
import importlib
print(hex(id(sys.modules["string"])))

importlib.reload(sys.modules["string"])

print(hex(id(sys.modules["string"])))
