# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy
        current = head.next
        current_sum = 0

        while current:
            if current.val == 0:
                cur.next = ListNode(current_sum)
                cur = cur.next
                current_sum = 0
            else:
                current_sum += current.val
            current = current.next
        return dummy.next