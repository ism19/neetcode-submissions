class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_dict = {}

        for i in range(len(nums)):
            nums_dict[nums[i]] = 1 + nums_dict.get(nums[i], 0)
        
        freq = [[] for i in range(len(nums) + 1)]

        for num, ct in nums_dict.items():
            freq[ct].append(num)

        res = []

        for i in range(len(freq) - 1, -1, -1):
            if len(res) == k:
                return res
            for num in freq[i]:
                res.append(num)


            
            
        