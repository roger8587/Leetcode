#2165. Smallest Value of the Rearranged Number
class Solution:
    def smallestNumber(self, num: int) -> int:
        num1 = list(str(abs(num)))
        if num <= 0:
            num1.sort(reverse = True)
            return -1*int(''.join(num1))
        else:
            num1.sort()
            for i,n in enumerate(num1):
                if n != '0':
                    temp = num1.pop(i)
                    break
            return int(temp+''.join(num1))

#133. Clone Graph
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node is None:
            return None
        clone_node = Node(node.val)
        # queue暫存
        cloned, queue ={node:clone_node}, [node]
        
        while queue:
            current = queue.pop(0)
            for neighbor in current.neighbors:
                if neighbor not in cloned:
                    queue.append(neighbor)
                    cloned_neighbor = Node(neighbor.val)
                    cloned[neighbor] = cloned_neighbor
                cloned[current].neighbors.append(cloned[neighbor])
        return cloned[node]

# 2. Add Two Numbers
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        current = 0
        result = ListNode(0)
        w = result
        while l1 or l2 or current > 0:
            if l1:
                current += l1.val
                l1 = l1.next
            if l2:
                current += l2.val
                l2 = l2.next
            w.next = ListNode(current % 10)
            current = current // 10
            w = w.next
        return result.next
    
# 61. Rotate List
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next: 
            return head
        cur = head
        n = 1
        while cur.next:
            cur = cur.next
            n += 1
        cur.next = head #形成一個環
        for i in range(n-k%n):
            cur = cur.next
        result = cur.next
        cur.next = None
        return result
