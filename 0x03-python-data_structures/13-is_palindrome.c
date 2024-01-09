#include "lists.h"
/**
  *
  *
  *
  *
  */
int is_palindrome(listint_t **head)
{
    listint_t *mid;
    listint_t *temp = *head;
  
    mid = midvalue(*head);
    mid = revrec(mid);
    while  (mid != NULL)
    {
        if (temp->n != mid->n)
            return (0);
        temp = temp->next;
        mid  = mid->next;
    }
    return (1);
}

listint_t* midvalue(listint_t *head)
{
    listint_t *sw;
    listint_t *ft;
    /*listint_t *new_node;*/
    sw = head;
    ft = head;

    if (head == NULL)
        /**head == NULL)*/
        return (head);
    while (ft && ft->next)
    {
        ft = ft->next->next;
        sw = sw->next;
    }
    /*new_node = sw;*/
    return (sw);
}

listint_t *revrec(listint_t *head)
{
    listint_t *temp;

    if (head == NULL || head->next == NULL)
            return (head);
    temp = revrec(head->next);
    head->next->next = head;
    head->next = NULL;
    return (temp);
}
