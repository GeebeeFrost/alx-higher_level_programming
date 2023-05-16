#include "lists.h"

/**
 * reverse_list - Reverses a linked list
 * @head: Address of pointer to head node
 *
 * Return: Pointer to first node of reversed list
 */
listint_t *reverse_list(listint_t **head)
{
	listint_t *prev, *temp, *next;

	if (!*head)
		return (NULL);
	if (!(*head)->next)
		return (NULL);
	prev = NULL;
	temp = *head;
	while (temp)
	{
		next = temp->next;
		temp->next = prev;
		prev = temp;
		temp = next;
	}
	*head = prev;
	return (*head);
}

/**
 * is_palindrome - Checks if a singly linked list is a palindrome
 * @head: Address of pointer to head node
 *
 * Return: 1 if it is a palindrome or 0 if it is not
 */
int is_palindrome(listint_t **head)
{
	listint_t *fast = *head, *slow = *head;

	if (!*head || !(*head)->next)
		return (1);
	/*
	 * Split list into two
	 * point slow to the node after the middle node
	 */
	while (fast && fast->next)
	{
		fast = fast->next->next;
		slow = slow->next;
	}
	/* allow for odd number of nodes */
	if (fast)
		slow = slow->next;
	/* Reverse second list */
	slow = reverse_list(&slow);
	fast = *head; /* return fast to beginning of first list */

	while (slow)
	{
		if (fast->n != slow->n)
			return (0);
		fast = fast->next;
		slow = slow->next;
	}
	return (1);
}
