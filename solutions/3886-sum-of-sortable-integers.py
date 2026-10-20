                    cnt += 1

            if cnt > 1:
                return False

            minMax.append((mini, maxi))

        for i in range(chunks - 1):
            if minMax[i][1] > minMax[i + 1][0]:
                return False

        return True

    def sortableIntegers(self, nums):
        n = len(nums)
        ans = 0

        i = 1
        while i * i <= n:
            if n % i == 0:
                if self.operation(i, nums):
                    ans += i

                if i != n // i:
                    if self.operation(n // i, nums):
                        ans += (n // i)
            i += 1

        return ans
