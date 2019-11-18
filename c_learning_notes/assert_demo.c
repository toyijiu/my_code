#include<assert.h>
#include<stdio.h>
#include<stdlib.h>

void test(int x)
{
    assert(x > 0);
    printf("%d\n",x);
}

int main()
{
    test(-1);
    return EXIT_SUCCESS;
}