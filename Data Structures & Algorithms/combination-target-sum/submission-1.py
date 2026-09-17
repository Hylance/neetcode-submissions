class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        nums.sort()
        def dfs(start, remaining):
            if remaining == 0:
                res.append(path.copy())
                return 
            for i in range(start, len(nums)):
                if nums[i] > remaining:
                    break
                path.append(nums[i])
                dfs(i, remaining - nums[i])
                path.pop()
        dfs(0, target)
        return res