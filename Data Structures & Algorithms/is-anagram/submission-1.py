class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = {}
        for i in s:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1

        for i in t:
            if i not in d:
                return False
            else:
                if d[i] == 1:
                    del d[i]
                else:
                    d[i]-=1

        if d == {}:
            return True
        else:
            return False