class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for i in strs:
            res += str(len(i))+"#"+i
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        l = 0
        while l < len(s):
            r = l
            while s[r] != "#":
                r+=1
            leg = int(s[l:r])
            val = s[r+1:r+1+leg]
            l = r+1+leg
            res.append(val)
        return res