# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curPrev , cur = None, head
        
        while cur:
            curNext,cur.next = cur.next, curPrev
            curPrev, cur = cur, curNext

        return curPrev
    