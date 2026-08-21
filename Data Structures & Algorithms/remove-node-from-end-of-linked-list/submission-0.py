# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        r = head
        for _ in range(n):
            r = r.next
        l = head
        prev = None
        while r:
            prev = l
            l = l.next
            r = r.next
        if prev:
            prev.next = l.next
        else:
            head = head.next
        return head
        
        