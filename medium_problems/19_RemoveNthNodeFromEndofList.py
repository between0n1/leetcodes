# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # 1. we must get the size of the linked list
        temp_node = head
        count = 0
        while (temp_node):
            count += 1
            temp_node = temp_node.next
        # count = size

        # 2. using the result (size) from step 1, we can now know whether we are in target_node or not. or furthermore, we can know whethere we are in previous node of the target node by counting.
        # 3. in the later while loop, if we are in previous node, we are gonna make a pointer than points to the previous_node.
        # 4. after step 3, now we are in the targetnode. so we do following: previous_node.next = target_node.next
        # 5. we break the while loop and return head_node.
        # 6. there are some corner cases.
        # 7. if targetnode is the first node of the linked list,
        # 8. we can easily return head.next

        target_count = (count - n + 1)
        previous_count = target_count - 1

        if (target_count == 1):  # || previous_count == 0
            return head.next

        prev_node = None
        temp_node = head
        count = 0

        while (temp_node):
            count += 1
            if (count == previous_count):
                prev_node = temp_node
            if (count == target_count):
                prev_node.next = temp_node.next
                return head
            temp_node = temp_node.next





