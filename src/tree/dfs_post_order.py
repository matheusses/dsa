def dfs_post_order(node):
    if not node:
        return

    dfs_post_order(node.left)
    dfs_post_order(node.right)
    print(node.val)