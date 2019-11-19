//确保对象在被使用前被初始化
//内置类型确保定义时初始化，其他的初始化责任在构造函数,构造函数要确保将对象的每一个成员初始化
#include <iostream>
#include <string>
#include <list>
class PhoneNumer{};

class ABEntry{
    public:
        ABEntry(const std::string& name,const std::string& address,const std::list<PhoneNumer>& phones);
    
    private:
        std::string theName;
        std::string theAddress;
        std::list<PhoneNumer> thePhones;
        int numTimesConsulted;
};

ABEntry::ABEntry(const std::string& name,const std::string& address,const std::list<PhoneNumer>& phones)
{
    theName = name;     //这些都是赋值而不是初始化。对象的成员初始化动作发生在进入构造函数本体之前，初始化发生在
                        //这些成员的default构造函数被自动调用之时，但是numTimesConsulted属于内置类型，不保证在这个赋值动作的时间点之前获得初值
                        //步骤是先调用default函数给成员设初值，再在这里赋值，default的操作多此一举
    theAddress = address;
    thePhones = phones;
    numTimesConsulted = 0;
}
//构造函数的一个比较好的写法是用成员初值列
ABEntry::ABEntry(const std::string& name,const std::string& address,const std::list<PhoneNumer>& phones)
:theName(name),         //现在这些对象的成员都是初始化，构造函数本体不会有任何动作，不会调用default构造函数
theAddress(address),
thePhones(phones),
numTimesConsulted(0)
{}
//总是使用成员初始列来初始化成员
//成员初始化次序总是先base classes,再derived classes
//C++对定义于不同编译单元内的non-local static对象的初始化相对次序无明确定义
