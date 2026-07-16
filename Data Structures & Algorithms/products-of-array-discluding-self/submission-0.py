class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix, suffix, ans = [1] * len(nums), [1] * len(nums), [1] * len(nums)
        for i in range(len(nums)):
            prefix[i] = prefix[i - 1] * nums[i - 1] if i > 0 else 1
        for i in reversed(range(len(nums))):
            suffix[i] = suffix[i + 1] * nums[i + 1] if i < len(nums) - 1 else 1
        for i in range(len(nums)):
            ans[i] = prefix[i] * suffix[i]
        return ans
        