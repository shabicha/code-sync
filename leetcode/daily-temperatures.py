class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        answer = [0] * len(temperatures)
        stack = [] #[[0,73], []]
        for i in range(len(temperatures)):
            #if not warmer than last day in stack, push on stack
            # if warmer than last day, pop - index manipulation to find # of days for that temp, keep popping until condition invalid 
            if stack and temperatures[i] < stack[-1][1]:
                stack.append([i, temperatures[i]])
            else:
                while stack and temperatures[i] > stack[-1][1]:
                    index, temp = stack.pop()
                    answer[index] = i - index
                stack.append([i, temperatures[i]])
        return answer