# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def getMiddle(head):
            dum = ListNode()
            dum.next = head
            slow = dum
            fast = dum

            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow

        def merge(l1, l2):
            dumm = ListNode()
            cur = dumm
            while l1 or l2:
                if not l1 and l2:
                    cur.next = l2
                    l2 = l2.next
                elif not l2 and l1:
                    cur.next = l1
                    l1 = l1.next
                else:
                    if l1.val < l2.val:
                        cur.next = l1
                        l1 = l1.next
                    else:
                        cur.next = l2
                        l2 = l2.next
                cur = cur.next
            return dumm.next

        def mergeSort(l):
            if l is None or l.next is None:
                return l

            mid = getMiddle(l)
            leftList = l
            rightList = mid.next
            mid.next = None
            leftList = mergeSort(leftList)
            rightList = mergeSort(rightList)
            return  merge(leftList, rightList)
        
        return mergeSort(head)
        



