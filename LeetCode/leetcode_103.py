# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
[Search Constraints]
if EvenLevel : right to left
if OddLevel : left to right
'''


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        result = []
        queue = []
        queue.append(root)
        level = 0

        while queue:
            level_values = []
            next_level = []
            level = level + 1
            for node in queue:
                level_values.append(node.val)

                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)

            if level % 2 == 0:
                level_values.reverse()

            result.append(level_values)
            queue = next_level

        return result

