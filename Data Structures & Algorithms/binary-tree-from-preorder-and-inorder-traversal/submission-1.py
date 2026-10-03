class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        # Map value -> index in inorder
        inorder_map = {}

        for i in range(len(inorder)):
            value = inorder[i]
            inorder_map[value] = i

        preorder_index = 0

        def dfs(left, right):
            nonlocal preorder_index

            if left > right:
                return None

            # First unused preorder value is the root
            root_val = preorder[preorder_index]
            preorder_index += 1

            root = TreeNode(root_val)

            # Find root in inorder
            mid = inorder_map[root_val]

            # Everything left of mid belongs to left subtree
            root.left = dfs(left, mid - 1)

            # Everything right of mid belongs to right subtree
            root.right = dfs(mid + 1, right)

            return root

        return dfs(0, len(inorder) - 1)
