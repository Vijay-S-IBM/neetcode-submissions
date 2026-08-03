class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0

        numset =set(nums)

        for i in nums:

            if i-1 not in numset:
                leg = 1
                while i+leg in numset:
                    leg+=1
                longest = max(longest , leg)
        return longest