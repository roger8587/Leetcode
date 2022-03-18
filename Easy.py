#171. Excel Sheet Column Number
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        Sum = 0
        for i in columnTitle:
            Sum = Sum*26 + ord(i)-64
        return Sum


#2164. Sort Even and Odd Indices Independently
class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        odd = nums[1::2]
        even = nums[::2]
        odd.sort(reverse = True)
        even.sort()
        result = []
        while odd or even:
            if even:
                result.append(even.pop(0))
            if odd:
                result.append(odd.pop(0))
        return result
    
#141. Linked List Cycle
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast==slow:
                return True
        return False
    
#21. Merge Two Sorted Lists
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(0)
        move = head
        if not list1: return list2
        if not list2: return list1
        while list1 and list2:
            if list1.val < list2.val:
                move.next = list1
                list1 = list1.next
            else:
                move.next = list2
                list2 = list2.next
            move = move.next
        move.next = list1 if list1 else list2
        return head.next

# 67. Add Binary

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        num_a, num_b = len(a)-1, len(b)-1
        current = 0
        res = []
        while num_a >= 0 or num_b >= 0:
            sum = current
            if num_a >= 0:
                sum+=int(a[num_a])
                num_a -= 1
            if num_b >=0:
                sum+=int(b[num_b])
                num_b -= 1
            current = sum // 2
            res.append(str(sum % 2))
        if current>0: res.append(str(current))
        res.reverse()
        return ''.join(res)
