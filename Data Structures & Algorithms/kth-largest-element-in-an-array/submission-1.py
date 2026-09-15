class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        '''
        If we maintain a heap of size k, then:
        the heap will always contain the k largest elements seen so far.
        the root of the heap (the smallest among these k) will be the k-th largest element.
        '''
        heapq.heapify(nums)
        while len(nums) > k:
            heapq.heappop(nums)
        return nums[0]