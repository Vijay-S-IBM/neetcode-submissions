class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        stack = [] #storing [num, index of the num]

        for i, num in enumerate(temperatures):
            while stack and num > stack[-1][0]:
                stackNum , stackIndex = stack.pop()
                res[stackIndex] = (i - stackIndex)
            stack.append([num, i])

        return res