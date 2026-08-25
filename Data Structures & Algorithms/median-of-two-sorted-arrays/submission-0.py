class Solution:
    def findMedianSortedArrays(
        self,
        nums1: List[int],
        nums2: List[int]
    ) -> float:

        A, B = nums1, nums2

        # 永远 binary search 较短的数组
        if len(A) > len(B):
            A, B = B, A

        m, n = len(A), len(B)

        l, r = 0, m
        half = (m + n + 1) // 2

        while l <= r:
            i = l + (r - l) // 2
            j = half - i

            Aleft = A[i - 1] if i > 0 else float("-inf")
            Aright = A[i] if i < m else float("inf")

            Bleft = B[j - 1] if j > 0 else float("-inf")
            Bright = B[j] if j < n else float("inf")

            # 找到正确 partition
            if Aleft <= Bright and Bleft <= Aright:

                # 奇数
                if (m + n) % 2:
                    return max(Aleft, Bleft)

                # 偶数
                return (
                    max(Aleft, Bleft)
                    + min(Aright, Bright)
                ) / 2

            # A 切得太靠右
            elif Aleft > Bright:
                r = i - 1

            # A 切得太靠左
            else:
                l = i + 1