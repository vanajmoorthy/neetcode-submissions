class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_length = 0

        for num in nums_set:
            max_for_each_num = 0
            if num - 1 in nums_set:
                continue
            else: 
                length = 1 
                while num + length in nums_set:
                    length += 1
                max_for_each_num = length
                
            if max_for_each_num > max_length:
                max_length = max_for_each_num
        
        return max_length
        