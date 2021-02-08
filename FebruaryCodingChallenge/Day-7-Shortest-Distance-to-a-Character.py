class Solution(object):
    def shortestToChar(self, s, c):
        """
        :type s: str
        :type c: str
        :rtype: List[int]
        """
        def getInd(string,char):
            try:
                return string.index(char)
            except:
                return 10000
        cList = []
        rev = s[::-1]
        length = len(s)
        for i in range(0, length):
            cList.append(min(getInd(s[i:], c), getInd(rev[(length-i-1):], c)))
        return cList        
