# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        h1 = list1
        h2 = list2

        

        output = head = ListNode()


        while h1 and h2:
            if h1.val <= h2.val:
                output.next = h1
                h1 = h1.next
            else:
                output.next = h2
                h2 = h2.next

            output = output.next

        if not h1:
            output.next = h2

        if not h2:
            output.next = h1


        return head.next
            
        