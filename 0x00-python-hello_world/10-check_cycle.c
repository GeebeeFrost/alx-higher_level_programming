#include "lists.h"

/**
 * check_cycle - Checks if a singly linked list has a cycle in it
 * @list: Pointer to head node
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	int count = 0, s_count;
	listint_t *fast, *slow;

	fast = list;
	while (fast)
	{
		count++;
		fast = fast->next;
		slow = list;
		s_count = 0;
		while (s_count < count)
		{
			if (slow == fast)
				return (1);
			slow = slow->next;
			s_count++;
		}
	}
	return (0);
}
