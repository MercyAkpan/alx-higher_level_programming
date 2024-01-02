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
	Ft = list->next->next;
	St = list->next;
	while (Ft && St && list)
	{
		Ft = Ft->next->next;
		St = St->next;
		if (Ft == St)
			return (1);
	}
	return (0);
}
