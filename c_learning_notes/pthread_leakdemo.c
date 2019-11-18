#include <stdio.h>
#include <pthread.h>
void* test(void* args)
{
    printf("%s\n",(char*)args);
    return (void*)0;
}

int main()
{
    pthread_t tid;
    pthread_create(&tid,NULL,test,"a");

    sleep(3);
    return 0;
}