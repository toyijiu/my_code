#python堆栈帧是对x86的模拟，用指针模拟BP,SP,IP寄存器
#可用sys._getframe(0)获取当前函数的堆栈帧，参数表示深度，1就是调用堆栈的上个函数堆栈帧
import sys
def save():
    f = sys._getframe(1)
    if not f.f_code.co_name.endswith("_logic"):
        raise Exception("Error!")
    print("ok")

def test():
    save()
def test_logic():
    save()


test_logic()
test()
