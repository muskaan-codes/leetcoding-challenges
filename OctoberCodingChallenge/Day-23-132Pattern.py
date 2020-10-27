class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        length = len(nums)
        if length < 3:
            return False
        right = float('-inf')
        stack = []
        for i in range(length-1, -1, -1):
            if nums[i] < right:
                return True
            else:
                while stack and stack[-1] < nums[i]:
                    right = stack.pop()
            stack.append(nums[i])
        return False
