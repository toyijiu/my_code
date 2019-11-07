#include<stdio.h>

//数组作为函数参数时，会被隐式地转换为指向数组第一个元素的指针，这时就无法用sizeof了
void test(int x[])
{
    printf("%d\n",sizeof(x));//4,即指针本身的位数，32位,此时的sizeof(x)实际上是sizeof(int*)
}

void test2(int* x)
{
    printf("%d",sizeof(x));//4
}

int main()
{
    int x[] = {1,2,3,4,5,6};
    printf("%d\n",sizeof(x));
    test(x);
    test2(x);
    return 0;
}