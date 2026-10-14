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
            return None 
        
        curr = head 
        o_t_n = {}

        while curr: 
            node = Node(x=curr.val)
            o_t_n[curr] = node 
            curr = curr.next 
        
        curr = head 
        while curr: 
            node = o_t_n[curr]
            if curr.next: 
                node.next = o_t_n[curr.next]
            if curr.random: 
                node.random = o_t_n[curr.random]
            curr = curr.next 
        
        return o_t_n[head]