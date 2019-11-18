#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>
#include <stdlib.h>
int main()
{
    for(int i=0;i<10;i++)
    {
        pid_t child = fork();

        //子进程操作
        if(child == 0)
        {
            printf("I am child process,child:%d,parent:%d,\n",getpid(),getppid());
            exit(0);
        }
        else if(child == -1)
        {
            perror("fork error");
        }
    }

    while(1)
    {
        pause();
    }
    return 0;
}