class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        max_dp = [0] * n
        min_dp = [0] * n
        res = max_dp[0] = min_dp[0] = nums[0]
        for i in range(1, n):
            max_dp[i] = max(nums[i], max_dp[i - 1] * nums[i], min_dp[i - 1] * nums[i])
            min_dp[i] = min(nums[i], min_dp[i - 1] * nums[i], max_dp[i - 1] * nums[i])
            res = max(res, max_dp[i])
        return res