# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return head
        temp = head
        while temp.next:
            new = ListNode(gcd(temp.val, temp.next.val))
            new.next = temp.next
            temp.next = new
            temp = new.next
        return head