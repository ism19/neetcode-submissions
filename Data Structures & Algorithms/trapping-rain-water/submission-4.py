class Solution:
    def trap(self, height: List[int]) -> int:
        left_max = [0] * len(height)
        right_max = [0] * len(height)
        trapped = 0

        left_max[0] = height[0]
        right_max[len(height) - 1] = height[len(height) - 1]

        for i in range(1, len(height) - 1):
            if left_max[i - 1] > height[i]:
                left_max[i] = left_max[i - 1]
            else:
                left_max[i] = height[i]
        
        for i in range(len(height) - 2, 0, -1):
            if right_max[i + 1] > height[i]:
                right_max[i] = right_max[i + 1]
            else:
                right_max[i] = height[i]
        
        for i in range(1, len(height) - 1):
            if left_max[i] < right_max[i]:
                trapped += left_max[i] - height[i]
            else:
                trapped += right_max[i] - height[i]
        
        return trapped

