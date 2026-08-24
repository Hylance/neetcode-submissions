class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findFirst():
            l, r = 0, len(nums) - 1
            res = -1
            while l <= r:
                m = (l + r) // 2
                if nums[m] == target:
                    res = m
                    r = m - 1
                elif nums[m] < target:
                    l = m + 1
                else:
                    r = m - 1
            return res
        def findLast():
            l, r = 0, len(nums) - 1
            res = -1
            while l <= r:
                m = (l + r) // 2
                if nums[m] == target:
                    res = m
                    l = m + 1
                elif nums[m] < target:
                    l = m + 1
                else:
                    r = m - 1
            return res
        return [findFirst(), findLast()]
        