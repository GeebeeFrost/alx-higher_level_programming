#include "lists.h"

/**
 * check_cycle - Checks if a singly linked list has a cycle in it
 * @list: Pointer to head node
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *fast, *slow;

	if (!list)
		return (0);
	fast = list;
	slow = list;
	while (fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}
	return (0);
}
