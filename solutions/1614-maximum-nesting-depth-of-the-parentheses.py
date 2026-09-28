class Solution:
    def maxDepth(self, s: str) -> int:

        for ch in s:
            if ch == "(":
                count += 1
            elif ch == ")":
                ans = max(ans, count)
        count = 0
        ans = 0
                count -= 1

        return ans
