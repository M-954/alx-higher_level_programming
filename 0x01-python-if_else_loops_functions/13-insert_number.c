#include "lists.h"
/**
 * insert_node - inserts a newnode in a sorted list
 * @head: pointer to the head pointer
 * @number: data to the new node
 *
 * Return: returns pointer to the newnode
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp;
	listint_t *newnode;

	temp = *head;
	newnode = malloc(sizeof(listint_t));
	if (newnode == NULL)
		return (NULL);

	newnode->n = number;
	newnode->next = NULL;

	if (*head == NULL || number < (*head)->n)
	{
		newnode->next = *head;
		*head = newnode;
		return (newnode);
	}

	while (temp->next != NULL && temp->next->n < number)
		temp = temp->next;

	newnode->next = temp->next;
	temp->next = newnode;
	return (newnode);
}
