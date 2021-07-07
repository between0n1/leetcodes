class Solution(object):

    def __init__(self):
        self.resultStart = 0
        self.resultLength = 0

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) < 2:
            return s
        for start in range(len(s)):
            self.expandRange(s, start, start)  # for odd length substring
            self.expandRange(s, start, start + 1)  # for even length substring
        return s[self.resultStart: self.resultStart + self.resultLength]

    def expandRange(self, s, start, end):
        while (start >= 0 and end < len(s) and
               s[start] == s[end]):
            start -= 1
            end += 1
        if (self.resultLength < end - start - 1):
            self.resultLength = end - start - 1
            self.resultStart = start + 1




