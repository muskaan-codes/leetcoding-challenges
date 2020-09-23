class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        def appearsNBy3(arr, n):
            arr.sort()
            number = arr[0]
            count = 0
            c = []
            for i in range(0,n):
                if arr[i] == number:
                    count += 1
                else:
                    count = 1
                    number = arr[i]
                if count> n/3 and number not in c:
                        c.append(number)
            return c
        length = len(nums)
        if length >= 1:
            return appearsNBy3(nums, length)
        else:
            return []
        
