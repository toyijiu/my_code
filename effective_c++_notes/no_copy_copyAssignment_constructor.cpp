//如果想禁止class自动生成copy constructor ,copy assignment,就声明一个private方法就行，
//如果想让错误前移置编译期，也可以设计一个专门的base class
class Uncopyable{
    protected:
        Uncopyable(){}
        ~Uncopyable(){}
    private:
        Uncopyable(const Uncopyable&);
        Uncopyable& operator=(const Uncopyable&);
};

class HomeForSale:private Uncopyable{
    
};