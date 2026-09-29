class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L, R = 0, len(nums) - 1
        while L <= R:
            M = (L + R) // 2
            
            # found
            if nums[M] == target:
                return M
            
            # on left sorted portion
            if nums[M] >= nums[L]:
                if target < nums[L] or target > nums[M]:
                    L = M + 1
                else:
                    R = M - 1
            # on right sorted portion
            else:
                if target > nums[R] or target < nums[M]:
                    R = M - 1
                else:
                    L = M + 1
        return -1
