"""You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing
together the nodes of the first two lists.

Return the head of the merged linked list."""


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        out = []

        min = list1.pop(0) if list1.pop(0) < list2.pop(0) else list2.pop(0)

        out.append(min)

        if len(list1) == 0 or len(list2) == 0:
            return out.extend(list1).extend(list2)

        out.append(self.mergeTwoLists(list1, list2))

        return out

        # this problem was supposed to use linked lists. I wrote the solution for
        # a list. Will revisit after more LL practice. I am not familiar with
        # the LL methods well enough
