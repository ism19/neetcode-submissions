class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)

        length = 1
        max = 0
        for num in nums:
            while num + length in seen:
                length += 1
            if length > max:
                max = length
            length = 1

        return max
        