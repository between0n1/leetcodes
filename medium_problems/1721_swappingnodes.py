# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution():
    def swapNodes(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        # O(n)
        # first while loop
        # 1. traverse linked list and increments INDEX
        # 2. if index == k, we will create a variable points to the node at the index and call it leftk
        # 3. at the end of this while loop, we now have the size of the linked list

        temp_node = head
        leftk = None
        index = 0
        while (temp_node):
            index += 1
            if (index == k):
                leftk = temp_node
            temp_node = temp_node.next
        size = index

        # corner cases
        # if listsize < k
        # return head

        # or if listsize is odd, and k is the midpoint of the list,
        # return head.

        if (size < k):
            return head
        if (size % 2 == 1 and (k == ((size // 2) + 1))):
            return head

        # 4. second while loop,
        # 5. we now have kth node from the beginning and size of the linked list.
        # 6. traverse again until we are in the target node ( kth node from the end of the linked list), called rightk
        # 7. swap leftk and rightk

        temp_node = head
        rightk = None
        index = 0
        while (temp_node):
            index += 1
            if (index == (size - k + 1)):  # in the target node
                rightk = temp_node
                temp_val = rightk.val
                rightk.val = leftk.val
                leftk.val = temp_val
                return head
            temp_node = temp_node.next










