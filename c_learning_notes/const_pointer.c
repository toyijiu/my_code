#include<stdio.h>

int main()
{
    int x[] = {1,2,3};

    // 修饰指针本身为常量,目标对象可修改
    int* const p1 = x;
    *(p1+1) = 22;
    printf("%d\n",x[1]);

    //修饰指向的目标对象为常量，指针本身可修改
    int const *p2 = x;
    p2++;
    printf("%d\n",*p2);
}