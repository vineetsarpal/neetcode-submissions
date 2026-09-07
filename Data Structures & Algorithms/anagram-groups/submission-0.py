class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # res = {}
        res = defaultdict(list) # using defaultdict so missing keys auto-create as [] instead of raising KeyError
        for s in strs:
            count = [0] * 26 # a...z [0,0,0,...26 zeros]
            for c in s:
                count[ord(c) - ord('a')] += 1
            # res[count].append(s)
            res[tuple(count)].append(s) # using tuple because lists are unhashable and can't be dict keys
        return list(res.values())