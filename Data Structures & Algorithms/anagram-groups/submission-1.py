class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]

        sorted_strs = ["".join(sorted(str)) for str in strs]

        words = {}

        for i in range(len(strs)):
            if sorted_strs[i] not in words:
                words[sorted_strs[i]] = []
            words[sorted_strs[i]].append(strs[i])
        
        grouped_strs = []

        for key in words:
            grouped_strs.append(words[key])

        return grouped_strs
