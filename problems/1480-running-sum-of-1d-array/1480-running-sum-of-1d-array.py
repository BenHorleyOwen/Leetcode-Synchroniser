class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        externalVar=0
        newList=[]
        for n in nums:
            externalVar+=n
            newList.append(externalVar)
        return newList