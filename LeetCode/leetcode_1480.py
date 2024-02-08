class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        tmp = 0

        for i in range(len(nums)):
            tmp = tmp + nums[i]
            result.append(tmp)

        return result