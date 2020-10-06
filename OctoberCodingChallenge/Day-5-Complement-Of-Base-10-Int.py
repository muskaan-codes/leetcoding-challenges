class Solution(object):
    def bitwiseComplement(self, N):
        """
        :type N: int
        :rtype: int
        """
        def swap(n):
            o = ""
            for x in n:
                if x == '0':
                    o+='1'
                else:
                    o+='0'
            return o
        
        first = bin(N).replace("0b","")
        return int(swap(first),2)
        
                    
        
