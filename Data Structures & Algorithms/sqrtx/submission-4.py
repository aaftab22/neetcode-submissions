class Solution:
    def mySqrt(self, x: int) -> int:
        left = 1
        right = x

        if x < 2:
            return x

        while left <= right:
            mid = (left+right) // 2

            result = mid*mid

            if result == x:
                return mid
            elif result > x:
                right = mid - 1
            else:
                left = mid + 1
        return right