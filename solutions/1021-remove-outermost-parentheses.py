class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        ans = ''
        c = 0

        for i in s:
            if i == "(":
                if c > 0:
                    ans += i
                c += 1
            else:
                c -= 1
                if c > 0:
                    ans += i

        return ans
