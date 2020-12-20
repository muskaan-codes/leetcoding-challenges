class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        mini = sys.maxint
        mid = sys.maxint
        for n in nums:
            if n <= mini:
                mini = n
            elif n <= mid:
                mid = n
            else:
                return True
        return False
