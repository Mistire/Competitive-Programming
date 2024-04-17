# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        dummy = ListNode()
        cur = dummy

        for i, head in enumerate(lists):
            if head:
                heappush(heap, (head.val, i, head))

        while heap:
            _, i, node = heappop(heap)
            cur.next = node
            cur = cur.next

            if node.next:
                heappush(heap, (node.next.val, i, node.next))
        return dummy.next
        
