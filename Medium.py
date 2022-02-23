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
