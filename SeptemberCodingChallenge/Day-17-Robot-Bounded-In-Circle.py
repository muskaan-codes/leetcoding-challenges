class Solution(object):
    def isRobotBounded(self, instructions):
        """
        :type instructions: str
        :rtype: bool
        """
        self.action = [[-1, 0], [0, -1], [1, 0], [0, 1]]
        self.index = 0
        self.currLocation = [50, 50]
        
        def turnLeft():
            if self.index != 0:
                self.index -= 1
            else:
                self.index = 3
                
        def turnRight():
            if self.index != 3:
                self.index += 1
            else:
                self.index = 0
                
        def goStraight():
            c, r = self.action[self.index]
            self.currLocation = [self.currLocation[0]+c, self.currLocation[1]+r]
            
        for i in instructions:
            if i == 'L':
                turnLeft()
            elif i == 'R':
                turnRight()
            else:
                goStraight()
            for x in self.currLocation: #It goes out of the circle plane here itself
                if x < 0 or x > 100:
                    return False
        if self.currLocation == [50, 50] or self.index != 0:
            return True
        else:
            return False
