"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        hashTable = {} # Key will be the the original node, Val Will be the new node
        resHead = prev = None
        cur = head
        while cur:
            newNode = Node(cur.val)
            if prev:
                prev.next = newNode
            else:
                resHead = newNode
            prev = newNode
            hashTable[cur] = newNode
            cur = cur.next
        cur = head
        while cur:
            curNewNode = hashTable[cur]
            if cur.random:
                curNewNode.random = hashTable[cur.random]
            cur = cur.next
        return hashTable[head]

        



        
