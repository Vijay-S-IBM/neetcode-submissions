class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numsset = set(nums)

        if len(numsset) == len(nums):
            return False
        else:
            return True