#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
 * insert_node - insert a number in a sorted linked list
 * @head: head of the list
 * @number: the number to be inserted
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current, *temp;
	int i = 0, j = 0;

	if (!(*head))
		return (NULL);
	current = *head;

	while (current->next)
	{
		if (current->n > number)
			break;
		current = current->next;
		i++;

	}
	current = *head;
	while(current->next)
	{
		if (j == i - 1)
		{
			temp = malloc(sizeof(listint_t));
			if (temp == NULL)
				return (NULL);
			temp->n = number;
			temp->next = current->next;
			current->next = temp;
			return (temp);

		}
		current = current->next;
		j++;
	}
	return (NULL);
}
