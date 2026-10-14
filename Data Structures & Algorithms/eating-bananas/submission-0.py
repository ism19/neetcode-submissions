class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        count = 0
        min_k = r
        while l <= r:
            count = 0
            mid = (r + l) // 2
            for pile in piles:
                if pile < mid:
                    count += 1
                else:
                    count += math.ceil(pile / mid)
            if count <= h:
                min_k = mid
                r = mid - 1
            else:
                l = mid + 1
        return min_k
