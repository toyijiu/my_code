#include<stdio.h>
#include<stdlib.h>
void test(int** x)
{
    int* p = malloc(sizeof(int));
    *p = 123;
    *x = p;
}

int main()
{
    int* x;
    test(&x);
    printf("%d\n",*x);
    free(x);
}