class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0 
        r = len(heights)-1
        result = 0

        while l < r:

            d = r - l
            m = min(heights[l], heights[r])
            volum = d * m


            if volum > result:
                result = volum
            if heights[l] > heights[r]:
                r-=1
            else:
                l+=1

        return result