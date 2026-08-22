class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
       res, cnt = 0, 0
       for num in nums:
         cnt = cnt + 1 if num == 1 else 0
         res = max(res, cnt)
       return res
            