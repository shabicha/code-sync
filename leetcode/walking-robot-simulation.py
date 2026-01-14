class Solution(object):
    def robotSim(self, commands, obstacles):
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """
        x=0
        y=0
        direction = 0
        dx = [0,-1,0,1]
        dy=[1,0,-1,0]
        maxVal=0
        obstaclesS= set(map(tuple, obstacles))


        for i in range(len(commands)):
            if commands[i] == -2:
                direction = (direction + 1)%4

            elif commands[i] ==-1:
                direction = (direction - 1)%4
            else:
                r=commands[i]
                while r>0:
                    x1 = x+ dx[direction]
                    y1=y+dy[direction]
                    if (x1,y1) in obstaclesS:
                        break
                    x=x1
                    y=y1
                    tempVal = x*x+y*y
                    maxVal = max(maxVal, tempVal)
    
                    r-=1

            
        return maxVal