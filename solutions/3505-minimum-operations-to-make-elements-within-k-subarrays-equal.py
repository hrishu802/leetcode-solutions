                sum_r += v

            elif len(left) < len(right):
                v = right.pop(0)
                left.add(v)
                sum_l += v
                sum_r -= v

            if i >= x - 1:
                mid = left[-1]
                ops[i] = (
                    mid * len(left) - sum_l
                    + sum_r - mid * len(right)
                )

        pre = [0] * (n + 1)

        for j in range(1, k + 1):
            cur = [inf] * (n + 1)

            for i in range(j * x, n + 1):
                cur[i] = min(
                    cur[i - 1],
                    pre[i - x] + ops[i - 1]
                )

            pre = cur

        return pre[n]
