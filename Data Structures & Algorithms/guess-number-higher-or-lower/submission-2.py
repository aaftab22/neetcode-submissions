class Solution:
    def guessNumber(self, n: int) -> int:
        left = 1
        right = n
        if n == 1:
            return 1
        while left <= right:
            mid = int((left+right) // 2)
            result = guess(mid)

            if result == 0:
                return mid
            elif result == -1:
                right = mid - 1
            else:
                left = mid + 1