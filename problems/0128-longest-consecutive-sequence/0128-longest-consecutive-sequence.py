class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = set(nums) #parses the list once and creates a hashmap for O(N)
        consec = 0
        for current in nums: #O(1) for looking up values in a map
            if current - 1 not in nums: #makes sure this is the start of a chain
                potential = current + 1 #value to check if its in the set
                while potential in nums:
                    potential += 1
                consec = max(consec, potential-current)
        return consec