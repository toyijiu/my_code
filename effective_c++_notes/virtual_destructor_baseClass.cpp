//当derived class对象经由一个base class指针被删除，而该base class带有一个non-virtual的析构函数，其结果未有定义。
//一般情况是对象的derived成分没有被销毁
//所以base class需要一个virtual析构函数，这样就允许derived class的实现得以客制化
//如果class不含virtual函数，通常表示它并不愿意用作一个base class，
//有virtual函数的对象会携带一个vptr(virtual table pointer)指针，vptr指针指向一个函数指针数组(vtbl),每个带有virtual函数的class都有一个对应的vtbl，当对象
//调用某一个virtual函数，实际上调用的函数取决于vtbl表中的地址(编译器指定)
//不要继承不带virtual析构函数的class，包括stl,string等容器

//定义pure virtual函数，即对应的class是abstract class，无法实例化对象，只能当base class，此时可将析构定义为pure virtual，但是必须为这个pure virtual函数提供一份定义，
//不需要多态的class不需要定义virtual析构函数，带多态性质的base class应该声明一个virtual析构函数，如果class带有任何virtual函数，就应该拥有一个virtual析构函数
class AWOV{
    public:
        virtual ~AWOV() = 0;
};
AWOV::~AWOV(){} //derived class调用析构时会一层层回溯直到调用base class的析构，不定义的话linker会抱怨