class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        numset = set(nums) #this makes O(N) but doesnt preserve list locations
        for n in numset:
            if (target-n) in nums: #if true, the value pair is found
                val1 = nums.index(n)
                nums[nums.index(n)]=None #stops duplicate values
                if (target-n) in nums:
                    val2 = nums.index(target-n)
                    return [val1,val2]