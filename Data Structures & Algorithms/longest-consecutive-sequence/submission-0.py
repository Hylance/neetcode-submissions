class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_set = set(nums)
        ans = 0
        for num in hash_set:
            if num - 1 not in hash_set:
                length = 1
                while num + length in hash_set:
                    length += 1
                ans = max(length, ans)
        return ans
                
        