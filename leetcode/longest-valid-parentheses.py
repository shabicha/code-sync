class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """

        maxLength =0

        #iterate, if ( add to stack, else check stack for removable, 
        #if ) check in stack for (, if in, add to temp else set temp length to 0
        stack =[-1]

        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            else:
                stack.pop()
                if stack:
                    
                    maxLength = max(maxLength, i - stack[-1])
                else:
                    stack.append(i)
            
                
        return maxLength