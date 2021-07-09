class Solution(object):
    def searchRange(self, nums, target):

        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        def first(nums, target):
            l = 0
            r = len(nums) - 1

            leftindex = -1
            while (l <= r):
                m = (r + l) // 2
                if (nums[m] == target):
                    leftindex = m
                    r = m - 1
                elif (nums[m] > target):
                    r = m - 1
                elif (nums[m] < target):
                    l = m + 1
            return leftindex

        def last(nums, target):
            l = 0
            r = len(nums) - 1

            rightindex = -1
            while (l <= r):
                m = (r + l) // 2
                if (nums[m] == target):
                    rightindex = m
                    l = m + 1
                elif (nums[m] > target):
                    r = m - 1
                elif (nums[m] < target):
                    l = m + 1
            return rightindex

        return ([first(nums, target), last(nums, target)])
