class Solution(object):
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        length1 = len(A)
        char = []
        if length1 == len(B):
            if A == B:
                for i in range(len(A)-1):
                    if A[i] in A[i+1:]:
                        return True
                return False
            elif sorted(A) == sorted(B):
                for i in range(length1):
                    if A[i] != B[i]:
                        char.append(i)
                        if len(char) > 2:
                            return False
                if len(char) == 2:
                    return(A[char[0]] == B[char[1]] and A[char[1]] == B[char[0]])
        return False
