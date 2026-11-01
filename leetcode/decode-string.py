class Solution:
    def isNumber(self, str):
        try:
            float(str)
            return True
        except ValueError:
            return False

    def decodeString(self, s: str) -> str:
        # [ = pop number before
        # ] = pop until [
        stack = [] #3, [, a, cc]
        i=0
        while i < len(s):
            if s[i] == "]":
                letter = '' #c
                while stack[-1] != "[":
                    letter = stack.pop() + letter 
                stack.pop()
                number = '' #2
                while stack and self.isNumber(stack[-1]):
                    number += stack.pop()
                number = number[::-1]
                number = int(number)
                stack.append(letter*number)
            else:
                stack.append(s[i])
            i+=1
        return ''.join(stack)