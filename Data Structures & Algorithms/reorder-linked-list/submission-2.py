# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head.next:
            return

        # Find middle
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        mid = slow
        # Reverse this second half
        prev = None
        cur = mid
        while cur and cur.next:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        cur.next = prev

        reverseHead = cur
        forwardCur = head
        reverseCur = reverseHead
        while forwardCur and forwardCur.next and reverseCur and reverseCur.next:
            tempForward = forwardCur.next
            forwardCur.next = reverseCur
            tempBack = reverseCur.next 
            reverseCur.next = tempForward
            forwardCur = tempForward
            reverseCur = tempBack
    


