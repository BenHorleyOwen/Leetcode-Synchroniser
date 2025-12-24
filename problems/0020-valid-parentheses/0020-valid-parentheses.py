class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        opens = ['(','{','[']
        closes = [')','}',']']
        stack = []
        if len(s)%2 != 0: return False
        for x in s:
            if x in opens: 
                stack.append(x) 
            elif x in closes and len(stack)>0:
                if opens.index(stack.pop(-1)) != closes.index(x): 
                    return False
            else:
                return False
        if len(stack)>0: return False
        return True