def dfs_in_order(node):
    if not node:
        return

    dfs_in_order(node.left)
    print(node.val)
    dfs_in_order(node.right)