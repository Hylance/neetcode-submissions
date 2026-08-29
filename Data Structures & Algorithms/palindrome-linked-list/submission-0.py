# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        # slow points to left mid after loop
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        prev = None
        while slow:
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp
        left, right = head, prev
        # len(right) = len(left) or len(left) + 1
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True

        