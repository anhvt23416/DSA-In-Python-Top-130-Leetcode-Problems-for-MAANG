class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxSofar = nums[0]
        currMax = nums[0]
        currMin = nums[0]
        for i in range(1,len(nums)):
            tempMax = max(nums[i], currMax*nums[i], currMin*nums[i])
            currMin = min(nums[i], currMax*nums[i], currMin*nums[i])
            currMax=tempMax
            maxSofar=max(currMax, maxSofar)
        return maxSofar