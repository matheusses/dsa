class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumOfLeftLeaves(self, root:[TreeNode]) -> int:
        
        left_values = []
        def dfs(count: int, node: [TreeNode]):
            if (node is None):
                return 
            if node.left is not None:
                left_values.append(node.left.val)
                dfs(count, node.left)
            dfs(count, node.right)
        dfs(left_values, root)

        return sum(left_values)
    
sol = Solution()
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(sol.sumOfLeftLeaves(root))