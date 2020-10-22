class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        # length = len(asteroids)
        # for i in range(length):
        #     if asteroids[i:]
        stack = []
        end = -1
        for newStar in asteroids: 
            if end == -1 or newStar > 0 or (newStar < 0 and stack[end] < 0):
                end += 1
                stack.append(newStar)
            elif newStar < 0 and stack[end] > 0: 
                oldStar = stack[end]
                if newStar + oldStar == 0: 
                    end += -1
                    stack.pop()
                else:
                    while oldStar > 0 and (newStar + oldStar < 0):
                        end += -1
                        stack.pop()
                        if end != -1: 
                            oldStar = stack[end]
                        else:
                            break
                    if (newStar + oldStar == 0 and end != -1):
                        end += -1
                        stack.pop()
                    elif (end == -1 or (oldStar + newStar) < 0):
                        end += 1
                        stack.append(newStar)
        if (end == -1):
            return []
        else:
            return stack
            
