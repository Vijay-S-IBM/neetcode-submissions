class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        sta = []

        for i in tokens:
            if i not in "+-*/":
                sta.append(int(i))
            else:
                a = sta.pop()
                b = sta.pop()
                if i == "+":
                    sta.append(a+b)
                elif i == "-":
                    sta.append(b-a)
                elif i == "*":
                    sta.append(a*b)
                else:
                    sta.append(int(b/a))
            
        return sta[-1]