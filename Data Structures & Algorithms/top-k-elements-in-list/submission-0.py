class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}

        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                d[i]+=1
        
        data = dict(sorted(d.items(), key = lambda items: items[1], reverse = True))

        fin_data = list(data.keys())

        return fin_data[0:k]


        