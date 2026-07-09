class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numbs = {}
        for i in range(len(nums)):
            numbs[nums[i]] = i
        
        for i in range(len(nums)):
            if (target - nums[i]) in numbs and numbs[target - nums[i]] != i:
                return [i, numbs[target - nums[i]]]
        
        return []