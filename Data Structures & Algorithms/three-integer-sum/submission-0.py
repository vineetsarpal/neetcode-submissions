class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, n in enumerate(nums):
            if i > 0 and n == nums[i - 1]:
                continue
            
            # 2 sum
            L, R = i + 1, len(nums) - 1
            while L < R:
                sum = nums[L] + nums[R] + n
                if sum > 0:
                    R -= 1
                elif sum < 0:
                    L += 1
                else:
                    res.append([n, nums[L], nums[R]])
                    L += 1
                    while L < R and nums[L] == nums[L - 1]:
                        L += 1
        return res               