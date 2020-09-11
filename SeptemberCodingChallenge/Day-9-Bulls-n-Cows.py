class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        bulls = 0
        cows = 0 
        length = len(secret)
        indexCounted = []
        for index in range(0, length):
            if secret[index] == guess[index]:
                bulls+=1
                indexCounted.append(index)
        for index in range(0, length):
            if secret[index] != guess[index]:
                if guess[index] in secret:
                    ind = [pos for pos, char in enumerate(secret) if char == guess[index]]
                    for i in ind:
                        if i not in indexCounted:
                            cows+=1
                            indexCounted.append(i)
                            break
        return "%sA%sB" % (bulls, cows)      
