class Solution(object):
    def reachNumber(self, target):
        """
        :type target: int
        :rtype: int
        """
        if target == 0:
            return 0
        elif target < 0:
            target = -target
        if target == 1:
            return 1
        else:
            step = 1
            current = 1
            while current < target or current % 2 != target % 2:
                step += 1
                current += step
            return step
