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
        ## 2 pass
        oldToCopy = { None: None }
        curr = head
        
        # Pass 1
        while curr:
            copy = Node(curr.val)
            oldToCopy[curr] = copy
            curr = curr.next
        
        # Pass 2
        curr = head
        while curr:
            copy = oldToCopy[curr]
            copy.next = oldToCopy[curr.next]
            copy.random = oldToCopy[curr.random]
            curr = curr.next
        return oldToCopy[head]

        # ## 1 Pass
        # oldToCopy = defaultdict(lambda: Node(0))
        # oldToCopy[None] = None
        # curr = head
        # while curr:
        #     oldToCopy[curr].val = curr.val
        #     oldToCopy[curr].next = oldToCopy[curr.next]
        #     oldToCopy[curr].random = oldToCopy[curr.random]
        #     curr = curr.next
        # return oldToCopy[head]