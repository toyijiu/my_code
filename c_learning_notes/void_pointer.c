//void*也叫万能指针，必须转型后才能进行对象操作，void* 指针可以和其他任何类型指针进行隐式转换
#include<stdio.h>

void test(void* p,int len)
{
    unsigned char *cp = p;
    for(int i=0;i<len;i++)
    {
        printf("0x%02x ",cp[i]);
    }
    printf("\n");
}

int main()
{
    int x = 0x00112233;
    test(&x,sizeof(x));
    return 0;
}