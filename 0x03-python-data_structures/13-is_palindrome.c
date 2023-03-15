#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: head if a list.
 * Return:	1 if list is a palindrome.
 *		0 if list is not a palindrome.
 */
int is_palindrome(listint_t **head)
{
	int size = 1;
	int j, i;
	int *array;

	if (!head)
		return (1);
	listint_t *current = *head;

	while (current->next)
	{
		current = current->next;
		size++;
	}

	array = malloc(sizeof(int) * size);

	i = j = 0;
	current = *head;
	while (current->next)
	{
		array[i] = current->n;

		if (i >= (size / 2))
		{
			if (current->n != array[j] && size % 2 == 0)
				return (0);
			i++;
			current = current->next;
			if (size % 2 != 0)
			{
				printf("i = %i, j = %i\n", i, j);
				if (current->n != array[j])
					return (0);
			}
			j--;
			continue;
		}
		i++;
		current = current->next;
		j = i - 1;
	}
	return (1);
}
