import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        data = list(re.sub(r'[^a-zA-Z0-9]', '', s).lower())
        l, r = 0, len(data) - 1

        while l < r:
            if data[l] != data[r]:
                return False
            l += 1
            r -= 1

        return True