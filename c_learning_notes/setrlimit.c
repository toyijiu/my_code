#include <sys/resource.h>

void test()
{
    char* s = "abc";
    *s = 'x';
}

int main()
{
    struct rlimit res = {.rlim_cur = RLIM_INFINITY,.rlim_max = RLIM_INFINITY};

    setrlimit(RLIMIT_CORE,&res);

    test();

    return 0;
}