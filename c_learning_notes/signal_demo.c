#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>
#include <signal.h>

void sig_test(int signo,siginfo_t* si,void* p)
{
    printf("signo:%d pid:%d value:%d\n",signo,si->si_pid,si->si_int);
}

void parent()
{
    //让子进程退出后自动回收，避免成为僵尸进程或者需要父进程 wait
    struct sigaction sat_cld =
    {
        /* data */
        .sa_handler = SIG_IGN,
        .sa_flags = SA_NOCLDWAIT
    };
    sigaction(SIGCHLD,&sat_cld,NULL);

    //注册信号处理程序
    struct sigaction sat_usr =
    {
        .sa_flags = SA_SIGINFO,
        .sa_sigaction = sig_test
    };
    sigaction(SIGUSR1,&sat_usr,NULL);

    //父进程一直循环
    while(true)
    {
        pause();
    }
    
}

void child()
{
    if(fork() == 0)
    {
        sleep(1);

        for(int i=0;i<10;i++)
        {
            //发送附加数据的信号
            sigqueue(getppid(),SIGUSR1,(union sigval){.sival_int = i});

            sleep(1);
        }

        exit(0);
    }
}

int main()
{
    child();
    parent();
    return 0;
}