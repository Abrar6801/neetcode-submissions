class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo, hi, res = 1, max(piles), max(piles)
        while lo<=hi:
            mid = (hi+lo)//2
            total_time = 0
            for p in piles:
                total_time += math.ceil(float(p)/mid)
            if total_time <= h:
                res = mid
                hi = mid-1
            else:
                lo =mid+1
        return res