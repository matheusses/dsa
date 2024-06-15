def dfs_post_order_k_ary(node):
    if not node:
        return

    for child in node.children:
        dfs_post_order_k_ary(child)
    print(node.val)