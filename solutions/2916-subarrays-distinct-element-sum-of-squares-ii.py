
        def push(node, l, r):
            if lazy[node] == 0 or l == r:
                return

            mid = (l + r) // 2
            val = lazy[node]

            apply(node * 2, l, mid, val)
            apply(node * 2 + 1, mid + 1, r, val)

            sum1[node] = (sum1[node] + val * length) % MOD
            lazy[node] = (lazy[node] + val) % MOD
                + val * val * length
            ) % MOD
        def apply(node, l, r, val):
            length = r - l + 1

            # Use the old sum1 before updating it
            sum2[node] = (
                sum2[node] + 2 * val * sum1[node]

        sum1 = [0] * (4 * n)   # Sum of distinct counts
        sum2 = [0] * (4 * n)   # Sum of squared distinct counts
        lazy = [0] * (4 * n)   # Lazy propagation

class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
