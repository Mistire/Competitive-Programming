# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur = head
        index = 0
        
        while cur:
            cur = cur.next
            index += 1
        count = 0

        dum = ListNode(0)
        dum.next = head
        temp = dum
        while count < index - n:
            temp = temp.next
            count += 1
        
        temp.next = temp.next.next

        return dum.next
        
        # cur = head
        
        # while n > 0:
        #     cur.next
        #     n -= 1

        # prev = head
        # while prev:
        #     prev = prev.next
        
        # cur.next = prev