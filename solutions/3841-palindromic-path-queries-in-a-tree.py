        for q in queries:
            parts = q.split()

            if parts[0] == "update":
                u = int(parts[1])
                new_char = parts[2]

                delta = char_mask(labels[u]) ^ char_mask(new_char)
                labels[u] = new_char

                fenwick_add(tin[u], delta)
                fenwick_add(tout[u] + 1, delta)

            else:  # path query
                u, v = int(parts[1]), int(parts[2])
                w = lca(u, v)

                path_mask = (
                    fenwick_prefix(tin[u])
                    ^ fenwick_prefix(tin[v])
                    ^ char_mask(labels[w])
                )

                # palindrome condition: ≤ 1 bit set
                answers.append(
                    path_mask == 0 or (path_mask & (path_mask - 1)) == 0
                )

        return answers
