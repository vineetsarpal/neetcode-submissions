class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): 
            return False

        s1count = Counter(s1)
        s2count = defaultdict(int)
        need, have = len(s1count), 0

        L = 0
        # add char at R
        for R in range(len(s2)):
            c = s2[R]
            s2count[c] += 1
            if c in s1count:
                if s2count[c] == s1count[c]:
                    have += 1
                elif s2count[c] == s1count[c] + 1:
                    have -= 1
        
            # when the window size exceeds
            if R - L + 1 > len(s1):
                c = s2[L]
                s2count[c] -= 1
                if c in s1count:
                    if s2count[c] == s1count[c]:
                        have += 1
                    elif s2count[c] == s1count[c] - 1:
                        have -= 1
                L += 1
            
            if have == need:
                return True

        return False
    
