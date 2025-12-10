class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        mi = m-1
        ni = n-1
        p = (m+n) - 1

        while ni >= 0:
            if mi>= 0 and nums1[mi] > nums2[ni]:
                nums1[p] = nums1[mi]
                mi -= 1

            else:
                nums1[p] = nums2[ni]
                ni -= 1

            p -= 1
      