#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>

/**
 * infinite_while - loop innfintio
 * void
 */
int infinite_while(void)
{
    while (1)
    {
        sleep(1);
    }
    return (0);
}

/**
 * main - retunr void
 * 
 */
int main(void)
{
    int pid, count = 0;
    while (count < 5)
    {
        pid = fork();
        if (pid == 0)
            exit(0);
        else if (pid > 0)
            printf("Zombie process created, PID: %d\n", pid);
        else
            exit(1);
        count++;
    }
    infinite_while();
    return (0);
}