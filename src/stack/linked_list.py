class Node():
    def __init__(self, val,next=None):
        self.val = val
        self.next = next


class Stack:

    def __init__(self):
        self.head = None

# aux => 1 -> None
# aux.next = None(head)

# 1 -> None

#---------------
# aux  => 2 -> None
# aux.next = 1 -> None

#  2 -> 1 -> None

# 3 -> 2 -> 1 -> None 



    def push(self, item):
        self.head = Node(item, self.head)

        # aux = Node(item)
        # aux.next = self.head
        # self.head = aux

    def pop(self):
        if self.is_empty():
            return None
        aux = self.head
        self.head = self.head.next

        return aux.val
           
    def peek(self):
        if self.is_empty():
            return None
        return self.head.val

    def is_empty(self):
        return self.head is None

