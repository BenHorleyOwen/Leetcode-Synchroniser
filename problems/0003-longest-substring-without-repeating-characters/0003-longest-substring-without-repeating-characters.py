class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        best = 0
        temp = []
        for right in s:
            while right in temp: #left pointer
                temp.pop(0)
            temp.append(right) #right pointer
            best = max(best, len(temp)) 
        return best