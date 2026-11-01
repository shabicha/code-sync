class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        stack = []
        for i in asteroids: 
            alive = True 
            while alive and stack and stack[-1] > 0 and i<0:
                prev = stack[-1]
                iAbsolute = i * -1
                if prev < iAbsolute:
                    stack.pop()
                elif prev == iAbsolute:
                    stack.pop()
                    alive = False
                else:
                    alive = False
            if alive:
                stack.append(i)
                
        return stack