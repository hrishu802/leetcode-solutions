class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        a = 0
        b = 0
        for i in nums:
            if i < target:
                a += 1
            elif i == target:
                b += 1
        ans = list(range(a, a + b))
        return ans
