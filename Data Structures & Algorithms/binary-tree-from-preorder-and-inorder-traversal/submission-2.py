class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inMap = {}

        for i in range(len(inorder)):
            inMap[inorder[i]] = i

        preIndex = 0

        def dfs(left, right):
            nonlocal preIndex

            if left > right:
                return None

            # Root is the next value in preorder
            rootVal = preorder[preIndex]
            preIndex += 1

            root = TreeNode(rootVal)

            # Find the root's position in inorder
            mid = inMap[rootVal]

            # Build left and right subtrees
            root.left = dfs(left, mid - 1)
            root.right = dfs(mid + 1, right)

            return root

        return dfs(0, len(inorder) - 1)