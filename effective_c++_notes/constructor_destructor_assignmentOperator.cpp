//对于一个empty class，编译器编译时会自动声明一个copy构造，一个copy assignment操作符和一个析构函数，如果你没有声明构造函数，
//编译器还会自动生成一个default构造，所有这几个都是public和inline的
//class Empty{}; 本质上等于
class Empty{
    //Empty(){}
    //Empty(const Empty& rhs){}
    //~Empty(){}
    //Empty& operator=(const Empty& rhs){}    //自动产生的析构函数时non-virtual的
};

int main()
{
    Empty e1; //default constructor
    Empty e2(e1); //copy constructor
    e2 = e1; //copy assignment
    return 0;
}