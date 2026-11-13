# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: # handle only when initial input is empty
            return None

        stack = [root]
        while stack:
            node = stack.pop()
            node.left, node.right = node.right, node.left

            # Handle edge case: when node is a leaf node -> not add into the stack
            # otherwise, it'd add None to the stack and get error when stack.pop and None has no node.right or node.left
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        return root

        