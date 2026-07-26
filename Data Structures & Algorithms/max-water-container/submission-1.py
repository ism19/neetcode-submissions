class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1
        max_amt = 0

        while i != j:
            height = min(heights[i], heights[j])
            if i < j:
                width = j - i
            if j < i:
                width = i - j
            area = width * height
            if max_amt < area:
                max_amt = area
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1

        return max_amt