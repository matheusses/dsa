def dfs_in_order_k_ary(node):
    if not node:
        return

    for i in range(0,len(node.children)//2):
        dfs_in_order_k_ary(node.children[i])
    print(node.val)
    for i in range(len(node.children)//2, len(node.children)):
        dfs_in_order_k_ary(node.right)