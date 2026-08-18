class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1Idx = {num : i for i, num in enumerate(nums1)}
        res = [-1] * len(nums1)
        stack = []
        for num in nums2:
            while stack and num > stack[-1]:
                val = stack.pop()
                res[nums1Idx[val]] = num
            if num in nums1Idx:
                stack.append(num)
        return res
        