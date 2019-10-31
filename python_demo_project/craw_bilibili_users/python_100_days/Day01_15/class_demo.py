import time
import os
class Student(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def study(self,course_name):
        print("%s正在学习%s" %(self.name,course_name))
    
    def watch_av(self,av_name):
        if self.age >= 18:
            print("%s正在看AV<%s>" %(self.name,av_name))
        else:
            print("%s未满18岁，乖乖看喜羊羊" %(self.name))

class Clock(object):
    def __init__(self,hour=0,minute=0,second=0):
        self.hour = hour
        self.minute = minute
        self.second = second
    
    def run(self):
        self.second += 1
        if self.second >= 60:
            self.second = 0
            self.minute += 1
            if self.minute >= 60:
                self.minute = 0
                self.hour += 1
                if self.hour >= 24:
                    self.hour = 0

    def show(self):
        print("%d时%d分%d秒" %(self.hour,self.minute,self.second))


if __name__ == "__main__":
    stu1 = Student("吴霄",27)
    stu1.study("毛选")
    stu1.watch_av("苍井空")

    clock = Clock(23,59,55)
    while True:
        os.system("cls")
        clock.show()
        time.sleep(1)
        clock.run()
    