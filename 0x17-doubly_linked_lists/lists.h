#ifndef LISTS_H
#define LISTS_H
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
/**
 * struct node - a defined datatype for a node
 * @n: data of type integer to be stored in the node
 * @next: pointer to the next node
 * @prev: pointer to the pevious node
 */
typedef struct node
{
	int n;
	struct node *next;
	struct node *prev;
} dlistint_t;
size_t print_dlistint(const dlistint_t *h);
#endif
