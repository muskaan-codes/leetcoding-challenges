class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        length = len(intervals)
        if length == 0 or not intervals[0]:
            return intervals
        intervals = sorted(intervals, key=lambda x: x[0])
        op = []
        tmp = intervals[0]
        for i in range(1, length):
            if intervals[i][0] > tmp[1]:
                op.append(tmp)
                tmp = intervals[i]
            else:
                tmp = [tmp[0], max(tmp[1], intervals[i][1])]
        op.append(tmp)
        return op
