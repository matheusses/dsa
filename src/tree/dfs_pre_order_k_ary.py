def dfs_pre_order_k_ary(node):
    if not node:
        return

    print(node.val)
    for child in node.children:
        dfs_pre_order_k_ary(child)
