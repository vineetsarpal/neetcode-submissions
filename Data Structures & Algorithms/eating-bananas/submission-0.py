class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Min eating speed has to be b/w 1 and max(piles)
        L, R = 1, max(piles)
        res = R
        
        while L <= R:
            k = (L + R) // 2
            hours = 0

            for p in piles:
                hours += math.ceil(p/k)
            
            if hours <= h:
                res = k
                R = k - 1
            else:
                L = k + 1
            
        return res
