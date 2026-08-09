class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq = {}
        for num in nums:
            freq[num] = 1 + freq.get(num,0)
        for num in freq.values():
            if num>1:
                return True
        return False
        