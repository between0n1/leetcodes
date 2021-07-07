class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        min_gap = 99999
        result = 0
        nums.sort()
        for i, num in enumerate(nums):
            l = i + 1
            r = len(nums) - 1
            while (l < r):
                cur_sum = num + nums[l] + nums[r]
                gap = target - cur_sum
                abs_gap = abs(gap)
                if (min_gap > abs_gap):
                    min_gap = abs_gap
                    result = cur_sum
                if (target > cur_sum):
                    l += 1
                elif (target < cur_sum):
                    r -= 1
                else:
                    return target;
        return result

