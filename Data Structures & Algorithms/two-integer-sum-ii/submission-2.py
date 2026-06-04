class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        visited = []

        for num in numbers:
            if target - num in visited:
                return [numbers.index(target-num) + 1, numbers.index(num) + 1]
            else:
                visited.append(num)
