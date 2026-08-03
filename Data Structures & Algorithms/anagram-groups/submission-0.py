class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}

        for i in strs:
            n = "".join(sorted(i))

            if n not in d:
                d[n] = [i]
            else:

                d[n].append(i)

        return list(d.values())
        