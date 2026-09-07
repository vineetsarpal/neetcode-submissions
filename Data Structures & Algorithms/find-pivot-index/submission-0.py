class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        Lsum = 0
        for i in range(len(nums)):
            Rsum = total - nums[i] - Lsum
            if Lsum == Rsum:
                return i
            Lsum += nums[i]
        return -1