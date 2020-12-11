class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        i=0
        j=len(arr)-1
        while i<j and (arr[i] < arr[i+1]):
            i+=1  
        while j>0 and (arr[j-1] > arr[j]):
            j-=1
        return i > 0 and j < len(arr)-1 and i==j
