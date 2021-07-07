class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """

        # if numRows == 1 : return s
        # if numRows == 2

        if numRows == 1:
            return s
        else:
            # if index + 1 % numRows == 0
            # it means we are in digonal.
            # if index + 1 % (numRows + (numRows - 2 ))
            # it means we are not anymore in diagonal.
            result = [""] * numRows
            index = 0
            row = 0
            step = 0
            while index < len(s):
                c = s[index]
                result[row] += c
                if ((step + 1) < numRows):
                    row += 1
                    step += 1
                elif (step + 1) >= numRows and (step + 1) < ((numRows + (numRows - 2))):
                    row -= 1
                    step += 1
                elif (step + 1) == (numRows + (numRows - 2)):
                    row = 0
                    step = 0
                index += 1
            print(result)
            return ''.join(result)


