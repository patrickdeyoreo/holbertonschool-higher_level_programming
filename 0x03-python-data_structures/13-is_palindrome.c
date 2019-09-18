#include "lists.h"

/**
 * _is_palindome - determine if a singly linked list is a palindrome (helper)
 * @head: a pointer to a pointer to the start of the list
 *
 * Return: 1 if the list is a palindrome, otherwise 0
 */
int _is_palindrome(listint_t **head, listint_t *tail)
{
	int status;

	if (!tail)
		return (1);

	status = _is_palindrome(head, tail->next);

	if (tail == *head || tail->next == *head)
	{
		*head = tail;
		return (status);
	}
	else if (status && (*head)->n == tail->n)
	{
		*head = (*head)->next;
		return (1);
	}
	return (0);
}


/**
 * is_palindome - determine if a singly linked list is a palindrome
 * @head: a pointer to a pointer to the start of the list
 *
 * Return: 1 if the list is a palindrome, otherwise 0
 */
int is_palindrome(listint_t **head)
{
	return (head && _is_palindrome(head, *head));
}
