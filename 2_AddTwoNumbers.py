# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        #
        carry = 0

        if (l1 == None or l2 == None):
            if l1 == None:
                return l2
            elif l2 == None:
                return l1
            else:
                return None
        else:
            new = ListNode()
            result = new
            while (l1 or l2):
                cur_sum = carry
                carry = 0
                if l1 != None:
                    cur_sum += l1.val
                    l1 = l1.next
                if l2 != None:
                    cur_sum += l2.val
                    l2 = l2.next
                if (cur_sum >= 10):
                    carry = 1
                    cur_sum = cur_sum % 10

                new.val = cur_sum

                if (l1 == None and l2 == None):
                    if (carry == 1):
                        new.next = ListNode(1)
                else:
                    new.next = ListNode()
                    new = new.next

            return result
