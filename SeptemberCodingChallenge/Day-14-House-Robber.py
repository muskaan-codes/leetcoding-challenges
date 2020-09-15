class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length > 1:
            incl = nums[0]
            excl = 0
            new_excl = 0
            for i in range(1, length):  
                new_excl = excl if excl>incl else incl 
                incl = excl + nums[i] 
                excl = new_excl 
            return max(excl, incl) 
        elif length == 1:
            return nums[0]
        else:
            return 0
