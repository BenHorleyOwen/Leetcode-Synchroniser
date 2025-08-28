class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        maxWealth=0
        for n in accounts:
            wealth=0
            for m in n:
                wealth+=m
            if wealth>maxWealth:
                maxWealth=wealth
        return maxWealth