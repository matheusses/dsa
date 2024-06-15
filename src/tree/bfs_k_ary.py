def bfs_k_ary(node):
    if not node:
        return

    queue = [node]
    while queue:
        current = queue.pop(0)
        print(current.val)
        for child in current.children:
            queue.append(child)
