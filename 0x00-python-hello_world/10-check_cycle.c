#include "lists.h"

/**
 * check_cycle - checks is a singly list has a cycle in it
 * @list: a singly list
 * Return: 1 if cycle found else 0
 */
int check_cycle(listint_t *list)
{
	listint_t *current = list;

	if (!list || !list->next)
		return (0);
	while (current->next)
	{
		if (current->next == list)
			return (1);
		current = current->next;
	}
	return (0);
}
