# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = prev = None
        carry = 0
        while l1 or l2:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

            sum = carry + val1 + val2
            carry = 1 if sum > 9 else 0
            sum = sum % 10
            newNode = ListNode(sum)
            if prev:
                prev.next = newNode
            else:
                head = newNode
            prev = newNode
        if carry == 1:
            prev.next = ListNode(carry)
        return head


        