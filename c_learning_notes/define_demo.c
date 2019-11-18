#include<stdio.h>
#define V1

#if defined(V1)
    int a = 0;
#else
    printf("New 2\n");
#endif

#undef V1