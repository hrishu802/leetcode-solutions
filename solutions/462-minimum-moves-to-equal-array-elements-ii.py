class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        ans = 0
        l = len(nums)

        nums.sort()

        for i in nums:
            ans += abs(t-i)


        t = nums[l//2]
        return ans
