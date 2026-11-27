            -1, l // 2)) / 2

    def get_val_at_idx(self, i, j, k, l, idx):
        if i > j:
            return self.b[k+idx]
        if k > l:
            return self.a[i+idx]

        idx_a = (j-i+1) // 2
        idx_b = (l-k+1) // 2

        ma = self.a[i+idx_a]
        mb = self.b[k+idx_b]
        
        if ma > mb:
            i, k = k, i
            j, l = l, j
            idx_a, idx_b = idx_b, idx_a
            ma, mb = mb, ma
            self.a, self.b = self.b, self.a

        max_idx_ma = idx_a + idx_b

        if max_idx_ma < idx:
            return self.get_val_at_idx(i+idx_a+1, j, k, l, idx - (idx_a + 1))
        else:
            return self.get_val_at_idx(i, j, k, k+idx_b-1, idx)
