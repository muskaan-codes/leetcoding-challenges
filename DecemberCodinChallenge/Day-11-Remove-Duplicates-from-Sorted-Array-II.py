class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for n in list(set(nums)):
            count = nums.count(n)
            if count > 2:
                while count > 2:
                    nums.remove(n)
                    count -= 1
                
