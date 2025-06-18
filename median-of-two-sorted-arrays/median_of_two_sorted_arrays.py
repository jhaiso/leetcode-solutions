from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(A) + len(B)
        half = total // 2

        if len(B) < len(A):
            A, B = B, A
        
        l, r = 0, len(A) - 1
        while True:
            ma = l + (r-l) // 2 # A
            mb = half - ma - 2  # B (-2 because both arrays are 0-indexed)

            Aleft = A[ma] if ma >= 0 else float("-inf")
            Aright = A[ma + 1] if ma + 1 < len(A) else float("inf")
            Bleft = B[mb] if mb >= 0 else float("-inf")
            Bright = B[mb+ 1] if mb + 1 < len(B) else float("inf")

            if Aleft <= Bright and Bleft <= Aright:
                if total % 2 == 1:
                    return min(Aright, Bright)
                else:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                r = ma - 1
            else:
                l = ma + 1