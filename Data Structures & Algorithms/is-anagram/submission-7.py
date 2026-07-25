class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        frequency = {}

        for i in s:
            if i in frequency:
                frequency[i] += 1
            else:
                frequency[i] = 1
        
        for i in t:
            if i in frequency:
                frequency[i] -= 1
            else:
                return False

        for value in frequency.values():
            if value != 0:
                return False

        return True
