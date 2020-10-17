class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        length = len(matrix[0])
        if length == 0:
            return False
        for x in matrix:
            if target>x[length-1]:
                continue
            else:
                if target in x:
                    return True
                else:
                    return False
        
