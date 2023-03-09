#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
 * index_l - returns the index of the ordered list
 * that number fits into
 * @current: is the head of the list
 * @number: a number
 * Return: the index of the list otherwise -1 when
 * number is greatest
 */
int index_l(listint_t *current, int number)
{
	int i = 0;

	while (current->next)
	{
		if (current->n > number)
			return (i);
		current = current->next;
		i++;
	}
	return (-1);
}

/**
 * insert_node - insert a number in a sorted linked list
 * @head: head of the list
 * @number: the number to be inserted
 *
 * Return: a pointer to the new node otherwise NULL
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current, *temp;
	int i = 0, j = 0;

	if (!(*head))
		return (NULL);
	current = *head;

	i = index_l(current, number);
	current = *head;
	temp = malloc(sizeof(listint_t));
	if (temp == NULL)
		return (NULL);
	temp->n = number;
	while (current->next)
	{
		if (i == 0)
		{
			temp->next = (*head)->next;
			(*head) = temp;
			return (temp);

		}
		if (i == -1)
		{
			free(temp);
			temp = add_nodeint_end(head, number);
			return (temp);
		}
		if (j == i - 1)
		{
			temp->next = current->next;
			current->next = temp;
			return (temp);
		}
		current = current->next;
		j++;
	}
	free(temp);
	return (NULL);
}
