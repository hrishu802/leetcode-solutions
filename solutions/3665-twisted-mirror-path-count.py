                else:

                    dp[i][j][1] = dp[i][j + 1][0]
                    dp[i][j][0] = dp[i + 1][j][1]
                if grid[i][j] == 1:

                    continue
                    dp[i][j][1] = 1
                    dp[i][j][0] = 1
                if i == n - 1 and j == m - 1:

            for j in range(m - 1, -1, -1):
        for i in range(n - 1, -1, -1):

        dp = [[[0, 0] for _ in range(m + 1)] for _ in range(n + 1)]

            return 1
                    ways = (
                        dp[i + 1][j][1] +
                        dp[i][j + 1][0]
                    ) % MOD
        if n == 1 and m == 1:

        m = len(grid[0])
        n = len(grid)

        MOD = 10**9 + 7
    def uniquePaths(self, grid: List[List[int]]) -> int:
class Solution:
