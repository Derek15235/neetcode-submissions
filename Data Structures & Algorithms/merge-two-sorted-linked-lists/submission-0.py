# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1Ptr = list1
        l2Ptr = list2
        res = prev = None
        while l1Ptr and l2Ptr:
            newNode = ListNode()
            if l1Ptr.val < l2Ptr.val:
                newNode.val = l1Ptr.val
                l1Ptr = l1Ptr.next
            else:
                newNode.val = l2Ptr.val
                l2Ptr = l2Ptr.next
            if not prev:
                prev = res = newNode
            else:
                prev.next = newNode
                prev = newNode
        if l1Ptr:
            if prev:
                prev.next = l1Ptr
            else:
                res = l1Ptr
        if l2Ptr:
            if prev:
                prev.next = l2Ptr
            else:
                res = l2Ptr
        return res
        
