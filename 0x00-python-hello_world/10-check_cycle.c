#include "lists.h"

/**
 * check_cycle - chquea si hay un ciclo en la lista
 * list - el puntero a la lista que nos pasan
 * Return: 0 si no es circular, 1 si es
 */

int check_cycle(lisint_t *list)
{
	listint_t *slow = list, *fast = list;

	if (list == NULL)
		return (0);

	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}

	return (0);
}
