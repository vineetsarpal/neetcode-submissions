class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        L, R = 0, len(nums) - 1
        while L <= R:
            # if the sub-arr is sorted already
            if nums[L] < nums[R]:
                res = min(res, nums[L])
                break
            M = (L + R) // 2
            res = min(res, nums[M])
            if nums[M] >= nums[L]:
                L = M + 1
            else:
                R = M - 1
        return res
            
