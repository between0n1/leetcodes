class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        leftptr = 0
        rightptr = len(height) - 1
        resultarea = 0
        # the value having smaller valued than another will move.

        while (leftptr < rightptr):

            leftvalue = height[leftptr]
            rightvalue = height[rightptr]

            if (resultarea < self.area(leftvalue, rightvalue, rightptr - leftptr)):
                resultarea = self.area(leftvalue, rightvalue, rightptr - leftptr)
            if (leftvalue < rightvalue):
                leftptr += 1
            elif (leftvalue > rightvalue):
                rightptr -= 1
            else:  # do not have to worry about whether we should move two pointers at the sametime or not because we use min(b1,b2)
                leftptr += 1
        return resultarea

    def area(self, b1, b2, dist):
        return (min(b1, b2)) * dist
    # 12685621


