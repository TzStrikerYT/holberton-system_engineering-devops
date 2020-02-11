#include <unistd.h>
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
	int i, son;

	for (i = 0; i < 5; i++)
	{
		son = fork();
		if (son > 0)
			printf("Zombie process created, PID: %u\n,", pid);
		else
			return (0);
	}
	infinite_while();
	return (0);
}
