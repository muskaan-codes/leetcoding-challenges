class Solution(object):
    def sequentialDigits(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: List[int]
        """
        from itertools import combinations
        a = []
        if len(str(low)) == len(str(high)):
            c = combinations([1,2,3,4,5,6,7,8,9], len(str(low)))
            a = list(c)
        else:
            for i in range(len(str(low)), len(str(high))+1):
                c = combinations([1,2,3,4,5,6,7,8,9], i)
                a += list(c)
        b = []
        for x in a:
            for i in range(0, len(x)):
                if i == 0:
                    prev = int(x[0])
                else:
                    if int(x[i]) == prev + 1:
                        prev = int(x[i])
                        if i == len(x) -1:
                            b.append(int(''.join(map(str, x))))
                        else:
                            continue
                    else:
                        break
        output = [x for x in b if low <= x <= high] 
        return output
