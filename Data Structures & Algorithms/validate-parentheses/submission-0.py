class Solution:
    def isValid(self, s: str) -> bool:
        d = {"{":"}", "[":"]", "(":")"}

        st = []

        for i in s:
            if i in d.keys():
                st.append(i)
            else:
                if st == []:
                    return False
                elif d[st[-1]] == i:
                    st.pop()
                else:
                    return False
        return st == []

        