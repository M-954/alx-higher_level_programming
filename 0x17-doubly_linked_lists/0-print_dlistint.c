#include "lists.h"
/**
 * print_dlistint - prints all the elements of a list
 * @h: pointer to the head
 *
 * Return: returns the number of nodes
 */
size_t print_dlistint(const dlistint_t *h)
{
	size_t count = 0;
	int element;

	while (h != NULL)
	{
		element = h->n;
		printf("%d\n", element);
		h = h->next;
		count++;
	}
	return (count);
}
