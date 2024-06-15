def dfs_pre_order(node):
    if not node:
        return

    print(node.val)
    dfs_pre_order(node.left)
    dfs_pre_order(node.right)