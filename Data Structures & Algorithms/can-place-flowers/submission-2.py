class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        leftclear = False 
        rightclear = False
        for i in range(len(flowerbed)):
            if n == 0: return True
            if flowerbed[i] == 0:
                if (i > 0 and flowerbed[i - 1] == 0) or i == 0: leftclear = True
                else: leftclear = False
                if (i < len(flowerbed) - 1 and flowerbed[i + 1] == 0) or i == len(flowerbed) - 1: rightclear = True
                else: rightclear = False
                if rightclear and leftclear:
                    flowerbed[i] = 1
                    n -= 1
            else: continue
        return n == 0