class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        a = len(nums)
        setA = set(nums)
        b = len(setA)
        if a != b:
            return True
        else:
            return False