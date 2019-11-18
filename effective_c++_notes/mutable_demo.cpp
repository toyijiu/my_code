#include <iostream>
#include <string.h>
//想在const成员函数中修改非static成员属性，就要用mutable字段
class CTextBlock{
    public:
        std::size_t length() const;
    
    private:
        char* pText;
        mutable std::size_t textLength;
        mutable bool lengthIsValid;
};

std::size_t CTextBlock::length() const
{
    if(!lengthIsValid)
    {
        textLength = strlen(pText);
        lengthIsValid = true;
    }
    return textLength;
}