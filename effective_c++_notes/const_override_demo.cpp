#include <string>
#include <string.h>
#include <iostream>

class TextBlock{
    private:
        std::string text;
    public:
        TextBlock(std::string input)
        {
            text = input;
        }
        //const成员函数不能更改对象内任何的non-static成员变量
        const char& operator[](std::size_t position) const
        {
            return text[position];
        }

        //返回值类型是reference to char,不是char
        char& operator[](std::size_t position)
        {
            return text[position];
        }
};


int main()
{
    TextBlock tb1("hello");
    std::cout<<tb1[0];
    //因为operator[]的返回值是reference to char，不是char，所以返回值可以做左值，返回值是内置类型char的话这个会编译失败
    tb1[0] = 'x';

    const TextBlock tb2("hello");
    std::cout<<tb2[0];
    //tb2[0] = 'x'; 错误 这里会调用const 的[]重载
    return 0;
}