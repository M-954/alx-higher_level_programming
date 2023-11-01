#include "lists.h"
/**
 * check_cycle - checks if linked list has a cycle
 * @list: pointer representing the head
 *
 * Return: returns 0 if no cycle and 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *first = list;
	listint_t *second = list;

	while (first != NULL && first->next != NULL)
	{
		second = second->next;
		first = first->next->next;
		if (second == first)
			return (1);
	}
	return (0);
}
