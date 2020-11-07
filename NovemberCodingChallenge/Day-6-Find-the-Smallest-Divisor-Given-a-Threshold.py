class Solution(object):
    def smallestDivisor(self, nums, threshold):
        """
        :type nums: List[int]
        :type threshold: int
        :rtype: int
        """
        def isDivided(nums, threshold, val):
            sum=0
            for i in nums:
              sum += (i+val-1)/val

            return threshold>=sum
        left = 1
        right = 1000000
        while(right > left):
            val = (right + left) / 2
            flag = isDivided(nums, threshold, val)
            if flag:
                right = val;
            else:
                left = val+1
        return left
