class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = 0
        max_length = 0
        seen = set()
        
        l = 0
        r = 0

        while r < len(s):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
                length -= 1
            seen.add(s[r])
            r += 1
            length += 1
            max_length = max(length, max_length)
        
        return max_length
            
