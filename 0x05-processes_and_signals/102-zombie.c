#include <unistd.h>
#include <sys/types.h>
#include <stdio.h>
#include <stdlib.h>
/**
 * infinite_while - infinite loop
 *
 * Return: 0
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
 * main - main function
 *
 * Return: 0 success
 */
int main(void)
{
	int i = 0;
	pid_t son;

	for (; i < 5; i++)
	{
		son = fork();
		if (son == 0)
		{
			dprintf(1, "Zombie process created, PID: %d\n",
				getpid());
			return (0);
		}
	}
	eternal();
	return (0);
}
