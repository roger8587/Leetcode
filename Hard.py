
#1359. Count All Valid Pickup and Delivery Options
class Solution:
    def countOrders(self, n: int) -> int:
        mod = 10**9+7
        result = 1
        n1 = n*2
        while n1>0:
            result*=n1
            n1-=1
        result = result//2**n
        return result%mod
