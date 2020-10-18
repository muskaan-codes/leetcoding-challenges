class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        range1 = len(s)-9
        output = []
        s1 = set()
        for i in range(range1):
            if s[i: i+10] in s1:
                output.append(s[i: i+10])
            else:
                s1.add(s[i: i+10])
        return set(output)
