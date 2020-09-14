class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        from collections import deque
        intervals.append(newInterval)
        intervals.sort()
        length = len(intervals)
        if length > 1:
            stack = deque() 
            stack.append(intervals[0])
            for x in range(0,length):
                if stack[-1][1] < intervals[x][0]:
                    stack.append(intervals[x])
                elif stack[-1][1] < intervals[x][1]:
                    temp = stack[-1]
                    stack.pop()
                    temp[1] = intervals[x][1]
                    stack.append(temp)
            return list(stack)
        else:
            return intervals
            
        
