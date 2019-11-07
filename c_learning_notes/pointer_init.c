#include<stdio.h>
//非自动周期指针变量或静态生存期指针变量必须用编译期常量表达式初始化
//全局数组
char s[] = "abc";
char* sp = s;

//变量变量
int x = 5;
int* xp = &x;

//函数
void test(){}
typedef void(*test_t)();

int main()
{
    static int* sx = &x;
    static test_t t = test;
    printf("%d\n",sizeof(s));

    return 0;
}

