#include <stdio.h>

int main()
{
    int a()
    {
        printf("a\n");
        return 1;
    }

    char* s()
    {
        printf("s\n");
        return "abc";
    }

    printf("call: %d,%s\n",a(),s());
    return 0;
}