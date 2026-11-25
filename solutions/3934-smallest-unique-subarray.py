            new_c = [0] * m

            p = new_p

            for x in reversed(pn):
                cl = c[x]
                count[cl] -= 1
                new_p[count[cl]] = x
                count[i] += count[i - 1]

            new_p = [0] * m
                count[c[x]] += 1

            for i in range(1, m):
            pn = [(x - k) % m for x in p]

            count = [0] * m
            for x in pn:

        k = 1
        while k < m:
        c = [0] * m
        for i in range(1, m):
            c[p[i]] = c[p[i - 1]] + (a[p[i]] != a[p[i - 1]])
        m = n + 1
        p = sorted(range(m), key=lambda i: a[i])

        a = [vals[x] for x in nums] + [0]

        # Build suffix array using counting sort

        # Coordinate compression
        vals = {v: i + 1 for i, v in enumerate(sorted(set(nums)))}
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)
class Solution:
