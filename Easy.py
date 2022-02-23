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
