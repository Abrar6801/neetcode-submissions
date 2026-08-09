class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums)-1
        while lo<hi:
            mid = lo + (hi-lo)//2
            if nums[mid] < nums[hi]:
                hi = mid
            else:
                lo = mid+1
        pivot = lo

        def binary_search(lo: int, hi: int) -> int:
            while lo<=hi:
                mid = lo + (hi-lo)//2
                if target == nums[mid]:
                    return mid
                elif target < nums[mid]:
                    hi = mid-1
                else:
                    lo = mid+1
            return -1
        
        result = binary_search(0,pivot-1)
        if result != -1:
            return result
        return binary_search(pivot,len(nums)-1)
        