#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - Inserts a number into a sorted linked list
 * @head: Address of pointer to head node
 * @number: Number to be inserted
 *
 * Return: Address of the new node or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *current;

	current = *head;
	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	new->n = number;
	new->next = NULL;
	if (!*head)
		*head = new;
	else
	{
		while (current && current->next && current->next->n < number)
			current = current->next;
		new->next = current->next;
		current->next = new;
	}
	return (new);
}
