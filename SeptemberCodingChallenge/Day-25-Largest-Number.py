class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        from functools import cmp_to_key
        
        def compare(x,y):
            if x+y<y+x:
                return 1
            elif x+y == y+x:
                return 0
            else:
                return -1
            
        for i in range(len(nums)):
             nums[i] = str(nums[i])
        nums.sort(key=cmp_to_key(lambda x,y:compare(x,y)))
        return "".join(nums).lstrip("0") or "0"
