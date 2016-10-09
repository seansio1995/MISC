#Given two arrays, write a function to compute their intersection.
#Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2].
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        intersection=[n1 for n1 in nums1 if n1 in nums2]
        return list(set(intersection))
