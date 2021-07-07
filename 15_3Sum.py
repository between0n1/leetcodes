class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result = []
        for i, num in enumerate(nums):
            l = i + 1
            end = len(nums) - 1
            target =  0 - num
            while ( l < end ):
                current = nums[l] + nums[end]
                if ( current < target):
                    l += 1
                elif (current > target):
                    end -= 1
                else:
                    temp_ = (num, nums[l], nums[end])
                    result.append(temp_)
                    l += 1
                    end -= 1
        return(set(result))