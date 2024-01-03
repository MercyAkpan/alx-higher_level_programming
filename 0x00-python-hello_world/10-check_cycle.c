#include "lists.h"
/**
  *
  *
  *
  *
  */
int check_cycle(listint_t *list)
{
	listint_t *Ft;
	listint_t *St;

	if (!list || !list->next)
		return (0);
	/*Ft = list->next->next;*/
	Ft = list->next;/*Ft points to what head of list points t0*/
	St = list;/*This points to head of list*/
	while (Ft && St && list && Ft->next)
	{
		Ft = Ft->next->next;
		St = St->next;
		if (Ft == St)
			return (1);
	}
	return (0);
}
