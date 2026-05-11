class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """

        stack =[]

        #iterate 
        i=0
        while i < len(s):
            #once ] pop until [
            Lstring = []
            Nstring = []
            if s[i] == "]":
                while stack and stack[-1] !="[":
                    j = stack.pop()
                    Lstring.append(j)
                stack.pop()
                while stack and stack[-1].isdigit():
                    k = stack.pop()
                    Nstring.append(k)
            #multiply and add
                Nstring.reverse()
                Lstring.reverse()

                part = int(''.join(Nstring)) * ''.join(Lstring)
                stack.append(part)
                i+=1
            else:
                stack.append(s[i])
                i+=1
        return ''.join(stack)