#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
 * index_l - returns the index of the ordered list
 * that number fits into
 * @head: is the head of the list
 * @number: a number
 * Return: the index of the list otherwise -1 when
 * number is greatest
 */
int index_l(listint_t **head, int number)
{
	listint_t *current = *head;
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
 * add_node_head - add a new node at the head of a list
 * @head: the head of the list
 * @number: data to store
 * Return: the new node
 */
listint_t *add_node_head(listint_t **head, int number)
{
	listint_t *new_node;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	new_node->n = number;

	new_node->next = (*head);
	*head = new_node;
	return (new_node);
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
	listint_t *temp, *current = *head;
	int i = 0, j = 0;

	if (!(*head))
	{
		temp = add_nodeint_end(head, number);
		return (temp);
	}
	i = index_l(head, number);
	if (i == 0)
	{
		temp = add_node_head(head, number);
		return (temp);
	}
	if (i == -1)
	{
		temp = add_nodeint_end(head, number);
		return (temp);
	}
	current = *head;
	while (current->next)
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
