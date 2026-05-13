# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        tmp_l1 = list1
        tmp_l2 = list2
        
        if not tmp_l1:
            return tmp_l2
        elif not tmp_l2:
            return tmp_l1
        elif not tmp_l1 and not tmp_l2:
            return

        if tmp_l1.val <= tmp_l2.val:
            start = tmp_l1
            tmp_l1 = tmp_l1.next
        else:
            start = tmp_l2
            tmp_l2 = tmp_l2.next
        current = start


        while tmp_l1 and tmp_l2:
            if tmp_l1.val <= tmp_l2.val:
                current.next = tmp_l1
                tmp_l1 = tmp_l1.next
            else:
                current.next = tmp_l2
                tmp_l2 = tmp_l2.next
            current = current.next

        while tmp_l1:
            current.next = tmp_l1
            current = current.next
            tmp_l1 = tmp_l1.next


        while tmp_l2:
            current.next = tmp_l2
            current = current.next
            tmp_l2 = tmp_l2.next

        print(tmp_l1, tmp_l2)

        return start



        
