from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Calculate the total length of both arrays
        length = len(nums1) + len(nums2)

        # If both arrays are empty, the median is 0 (edge case)
        if length == 0:
            return 0

        # Combine both arrays and sort them in ascending order
        arr = nums1 + nums2
        arr.sort()

        # Calculate the median based on the length of the combined array
        if length % 2 == 0:
            # If the total length is even, take the average of the middle two elements
            return (arr[int(length / 2) - 1] + arr[int(length / 2)]) / 2
        else:
            # If the total length is odd, return the middle element as the median
            return arr[int(length / 2)]
