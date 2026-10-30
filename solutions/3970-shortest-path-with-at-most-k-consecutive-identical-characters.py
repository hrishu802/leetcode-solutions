        for u, v, w in edges:
            g[u].append((v, w))
        best = [[float("inf")]*k for _ in range(n)]
        pq = []
        pq.append((0, 0, 0))
        best[0][0] = 0        

        while len(pq):
            d, u, cons = heapq.heappop(pq)
            if d > best[u][cons]:
                continue
            for v, w in g[u]:    
                if labels[u] == labels[v]:
                    if cons+1 < k and best[u][cons]+w < best[v][cons+1]:
                        best[v][cons+1] = best[u][cons]+w
                        heapq.heappush(pq, (best[v][cons+1], v, cons+1))
                else:
                    if best[u][cons]+w < best[v][0]:
                        best[v][0] = best[u][cons]+w
                        heapq.heappush(pq, (best[v][0], v, 0))
        res = float("inf")
        for i in range(k):
            res = min(res, best[n-1][i])

        if res == float("inf"):
            return -1
                
        return res
