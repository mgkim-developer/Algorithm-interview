# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        slow = fast = head

        while fast and fast.next:
            # 1 step
            slow = slow.next
            # 2 step
            fast = fast.next.next

        return slow
