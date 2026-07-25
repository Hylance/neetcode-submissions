class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = defaultdict(int)
        maxCount = 0
        ans = -1
        for num in nums:
            count[num] += 1
            if maxCount < count[num]:
                maxCount = count[num]
                ans = num
        return ans
        