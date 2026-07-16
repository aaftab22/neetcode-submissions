class Solution:
    
    def validPalindrome(self, s: str) -> bool:
        first = 0
        last = len(s)-1

        def isPalindrome(first, last):
            while first < last:
                if s[first] == s[last]:
                    first += 1
                    last -= 1
                else:
                    return False
            return True

        while first < last:
            if s[first] == s[last]:
                first += 1
                last -= 1
            else:
                return (
                    isPalindrome(first + 1, last) or
                    isPalindrome(first, last - 1)
                )
        return True