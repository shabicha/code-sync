class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        hashMap = {"(":")", "[":"]", "{":"}"}
        stack =[]
        for i in s:
            if i in hashMap:
                stack.append(hashMap[i])
            else:
                if stack and stack[-1] != i:
                    return False
                elif stack:
                    stack.pop()
                else:
                    return False

        if len(stack) ==0:
            return True
        return False