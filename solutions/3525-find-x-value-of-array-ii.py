                update(node * 2, l, mid, idx, value)
            else:
                update(node * 2 + 1, mid + 1, r, idx, value)

            tree[node] = merge(tree[node * 2], tree[node * 2 + 1])

        def query(node, l, r, ql, qr):
            if ql <= l and r <= qr:
                return tree[node]

            mid = (l + r) // 2

            if qr <= mid:
                return query(node * 2, l, mid, ql, qr)

            if ql > mid:
                return query(node * 2 + 1, mid + 1, r, ql, qr)

            left = query(node * 2, l, mid, ql, qr)
            right = query(node * 2 + 1, mid + 1, r, ql, qr)

            return merge(left, right)

        build(1, 0, n - 1)

        result = []

        for index, value, start, x in queries:
            update(1, 0, n - 1, index, value)

            _, pref = query(1, 0, n - 1, start, n - 1)

            result.append(pref[x])

        return result
