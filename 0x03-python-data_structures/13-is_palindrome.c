#include "lists.h"
/**
 * reverse - reverses a linkedlist
 * @head: pointer to head
 *
 * Return: pointer
 */

listint_t *reverse(listint_t *head)
{
  listint_t *prev = NULL;
  listint_t *current = head;
  listint_t *next = NULL;

  while (current != NULL)
  {
      next = current->next;
      current->next = prev;
      prev = current;
      current = next;
  }
  return prev;
}

/**
 * is_palindrome - checks for palindrom
 * @head: pointer to head node
 *
 * Return: 1 or 0
 */
int is_palindrome(listint_t **head)
{
 listint_t *slow = *head;
 listint_t *fast = *head;
 listint_t *second_half = NULL;
 listint_t *first_half = NULL;
 listint_t *temp = NULL;

 if (*head == NULL || (*head)->next == NULL)
     return 1;

 while (fast != NULL && fast->next != NULL)
 {
     fast = fast->next->next;
     temp = slow;
     slow = slow->next;
 }

 second_half = slow;
 first_half = *head;

 if (fast != NULL)
 {
     temp = slow;
     slow = slow->next;
 }

 temp->next = NULL;

 second_half = reverse(second_half);

 while (second_half != NULL)
 {
     if (first_half->n != second_half->n)
         return 0;
     first_half = first_half->next;
     second_half = second_half->next;
 }

 return 1;
}
