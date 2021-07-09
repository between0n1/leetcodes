class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        # from end of the list, find the first decreasing position
        # from position + 1 to end, find next ÷greater integer
        # [posiiton], greater integer =  greater integer, [posiiton]
        # reverse(posiiton + 1, end) because they are descending order when reading from left to right

        def reverse(nums, l, r):
            while (l < r):
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

        end = len(nums)
        pointer = end - 1
        target_left = - 1
        target_right = end - 1

        while (pointer > 0 and nums[pointer] <= nums[pointer - 1]):
            pointer -= 1

        if (pointer != 0):
            target_left = pointer - 1
            smallest_diff = 999
            while (pointer < end):
                cur_diff = nums[pointer] - nums[target_left]
                if (cur_diff > 0 and nums[pointer]):
                    if (smallest_diff >= cur_diff):
                        smallest_diff = cur_diff
                        target_right = pointer
                pointer += 1
            nums[target_left], nums[target_right] = nums[target_right], nums[target_left]
        reverse(nums, target_left + 1, end - 1)


