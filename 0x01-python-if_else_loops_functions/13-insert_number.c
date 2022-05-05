#include <stdio.h>
#include <stdlib.h>
#include <stddef.h>
#include "lists.h"

/**
 * insert_node - insertar un nuevo nodo
 * @head: asd
 * @num: asd
 * Return - asdsd
 */

listint_t *insert_node(listint_t **head, int num)
{
	listint_t *current;
	listint_t *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = num;
	new->next = NULL;

	if (*head == NULL)
	{
		*head = new;
		return (new);
	}
	current = *head;

	while (current->next != NULL && current->next->n < num)
			current = current->next;
	if (current->n > new->n)
	{
		new->next = *head;
		*head = new;
		return (new);
	}
	new->next = current->next;
	current->next = new;
	return (new);
}

