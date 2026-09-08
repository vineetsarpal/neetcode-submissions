class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Hashmap with key = num, val = count of occurences of each num
        count = {}

        # Array with index = count of occurences of each num, val = array of nums that occur that many. times 
        freq = [ [] for i in range(len(nums) + 1)]

        # fill the hashmap
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        # iterate the hashmap and fill freq
        for n, c in count.items():
            freq[c].append(n)
        
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
            

           