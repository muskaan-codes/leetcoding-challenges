class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        points.sort()
        ans = 1
        if points == []:
            return 0
        max1 = points[0][1]
        for i,j in points[1:]:
            if max1 < i:
                ans += 1
                max1 = j
            if j < max1:
                max1 = j
        return ans
