class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        longest = 0

        for n in numsSet:
            if n-1 not in numsSet:
                # start of a sequence
                seqLen = 1
                # check next in sequence
                while n + seqLen in numsSet:
                    seqLen += 1
                longest = max(longest, seqLen)
        return longest