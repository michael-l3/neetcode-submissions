class Solution:
    def diameterOfBinaryTree(self, root):
        diameter = 0

        def height(node):
            nonlocal diameter

            if not node:
                return 0

            left = height(node.left)
            right = height(node.right)

            # Longest path passing through this node
            diameter = max(diameter, left + right)

            # Height of current node
            return 1 + max(left, right)

        height(root)
        return diameter
