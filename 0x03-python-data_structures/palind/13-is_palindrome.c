#include "lists.h"
#include <stdio.h>

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: head if a list.
 * Return: 1 if list is a palindrome.
 * 	   0 if list is not a palindrome.
 */
int is_palindrome(listint_t **head)
{
	int i = 0;
	listint_t *current = *head;

	while (current->next)
	{
		current = current->next;
		i++;
	}
	printf(" i = %d\n", i);
	return 1;
}
