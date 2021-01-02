class Solution(object):
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        nums = [int(x) for x in str(n)]
        i = j = len(nums)-1
        while i>0 and nums[i-1]>=nums[i]:
            i-=1
        if i==0:
            return -1
        i-=1   
        while nums[j]<=nums[i]:
            j-=1
        nums[j], nums[i] = nums[i], nums[j]
        l, r = i+1, len(nums)-1
        while l<r:
            nums[l], nums[r] = nums[r], nums[l]
            l+=1
            r-=1
        final = int("".join(str(x) for x in nums))
        return final if final<2**31 else -1
        
