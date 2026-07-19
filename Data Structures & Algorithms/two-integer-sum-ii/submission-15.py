class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        first, last = 0, len(numbers) - 1
         

        while first < last:
            if numbers[first] + numbers[last] == target:
                return [first+1,last+1]
            else:
                if target > numbers[first] + numbers[last]:
                    first += 1
                else:
                    last -= 1
        return numbers