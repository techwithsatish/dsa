question 52: https://www.structy.net/problems/binary-tree-warm-up

# Get ready for the upcoming binary tree problems by watching us implement a node class.

`class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")


#   a
#   /\
#   b c
#  /\  \
# d e   f


a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

print(c.right)
print(f)`


