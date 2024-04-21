# def pow(x, n):
#     result = 1

#     for _ in range(0, n):
#         result *= x

#     return result

# print(pow(2, 3))


# def pow(x, n):
#   if (n == 1):
#     print(f'x: {x}, n: {n}')
#     return x
#   else: 
#     print(f'x: {x}, n: {n}')
#     return x * pow(x, n - 1)

# print(pow(2, 3))

# 2³

from linked_list import Stack
def pow(x, n):
    stack = Stack()
    result = 1
    for _ in range(n):
        stack.push(x)

    while not stack.is_empty(): 
        result *= stack.pop()

    return result

print(pow(2, 3))



 
 
 