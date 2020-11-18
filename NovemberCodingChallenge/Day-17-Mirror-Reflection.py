import math
class Solution(object):
    def mirrorReflection(self, p, q):
        """
        :type p: int
        :type q: int
        :rtype: int
        """
        def gcd(x,y):
            while(y): 
                x, y = y, x % y 
            return x
        return abs(~(not((q // gcd(p, q) * p // q) % 2))) if (q // gcd(p, q)) % 2 else 0
