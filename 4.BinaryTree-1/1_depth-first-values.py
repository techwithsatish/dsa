# q53: https://www.structy.net/problems/depth-first-values

class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def depth_first_values(root):
    if root is None:
        return
    values = []
    stack = [root]

    while stack:
        current = stack.pop()
        values.append(current.val)

        if current.right:
            stack.append(current.right)

        if current.left:
            stack.append(current.left)

    print(values)

depth_first_values(None)
#   -> []















