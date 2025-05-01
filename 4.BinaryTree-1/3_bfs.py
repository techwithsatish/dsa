from collections import deque


class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None


a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#      a
#    /   \
#   b     c
#  / \     \
# d   e     f




def breadth_first_values(root):
    if root is None:
        return []
    d = deque()
    d.append(root)
    values = []
    while d:
        current = d.popleft()
        values.append(current.val)
        if current.left:
            d.append(current.left)
        if current.right:
            d.append(current.right)

    return values


breadth_first_values(a)
#    -> ['a', 'b', 'c', 'd', 'e', 'f']
