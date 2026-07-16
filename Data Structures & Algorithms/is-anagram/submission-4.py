class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        strs = {}
        strt = {}
        for i in s:
            if i in strs:
                strs[i] += 1
            else:
                strs[i] = 1

        for i in t:
            if i in strt:
                strt[i] += 1
            else:
                strt[i] = 1
        
        if strs == strt:
            return True
        else:
            return False