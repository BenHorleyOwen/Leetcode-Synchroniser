class Solution(object):
    def numberOfSteps(self, num):
        """
        :type num: int
        :rtype: int
        """
        output=0
        while num!=0:
            if num%2==0: num=num/2
            else: num-=1
            output +=1
        return output