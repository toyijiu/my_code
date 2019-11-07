#include<stdio.h>

//如果数组有自动生存周期且没有static修饰符，可以用非常量表达式来定义数组
/*
数组初始化规则
1.如果是静态生存周期，必须是常量表达式
2.如果提供初始化器，可以不提供数组长度，由初始化器的最后一个元素决定
3.如果同时提供⻓度和初始化器，那么没有提供初始值的元素都被初始化为 0 或 NULL
*/

void test(int n)
{
    //初始化器
    int x[n];
    for(int i=0;i<n;i++)
    {
        x[i] = i;
    }

    struct data {int x[n];} d;
    printf("%d\n",sizeof(d));
}

//初始化特定的元素
void test2()
{
    int x[] = {0,1,[6] = 6,7,8};
    int len = sizeof(x)/sizeof(int);
    for(int i=0;i<len;i++)
    {
        printf("%d\n",x[i]);
    }
}

int main()
{
    int x[] = {1,2,3,4};
    printf("%d\n",sizeof(x));

    test2();
    return 0;
}