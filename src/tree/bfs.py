def bfs(node):
    if not node:
        return

    queue = [node]
    while queue:
        current = queue.pop(0)
        print(current.val)
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)