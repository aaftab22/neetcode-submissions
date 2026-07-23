class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = []
        for i in range(len(nums)):
            if nums[i] in seen:
                for j in range(i):
                    if nums[j] == nums[i] and abs(i - j) <= k:
                        return True
            seen.append(nums[i])

        return False