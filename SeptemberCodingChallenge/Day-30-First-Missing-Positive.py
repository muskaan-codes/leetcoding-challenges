class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = list(set(nums))
        nums.sort()
        length = len(nums)  
        if length == 0:
            return 1
        elif length == 1:
            return 2 if nums[0] == 1 else 1
        allNegative = True
        for i in range(length): 
            if allNegative:
                if nums[i] > 0:
                    allNegative = False
                    if nums[i] > 1:
                        return 1
            else:
                if nums[i-1] + 1 == nums[i]:
                    continue
                else:
                    return nums[i-1] + 1
        if allNegative:
            return 1
        return nums[-1] + 1
        
