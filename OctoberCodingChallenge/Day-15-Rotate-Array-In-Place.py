class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        k = k % length
        tmp = nums
        tmp = tmp[-k:] + tmp[:-k]
        print(tmp)
        for i in range(length):
            nums[i] = tmp[i]
