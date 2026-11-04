class Solution:
    def isHappy(self, n: int) -> bool:
        cache = set()
        

        while n not in cache:
            cache.add(n)
            total = 0
            while n>0:
                total += (n%10)**2
                n = n//10
            
            n = total
            if total == 1:
                return True
        return False