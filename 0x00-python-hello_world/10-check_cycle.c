#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
/**
* check_cycle - Checks if a singly linked list has a cycle in it.
* @list: the singly linked list
* Return: 0 if there is no cycle, 1 if there is a cycle
*/
int check_cycle(listint_t *list)
{
	listint_t *current;
	listint_t *head;

	current = list->next;
	head = list->next->next;

	if (current == NULL || current->next == NULL)
		return (0);

	while (current != NULL && head)
	{
		if (current == head)
			return (1);
		current = current->next;
		head = head->next->next;
	}
	return (0);
}
