class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res, curSum = 0, 0
        prefixSumCounts = {0 : 1}
        for num in nums:
            curSum += num
            diff = curSum - k
            res += prefixSumCounts.get(diff, 0)
            prefixSumCounts[curSum] = 1 + prefixSumCounts.get(curSum, 0)
        return res