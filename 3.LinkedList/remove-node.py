class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f

# a -> b -> c -> d -> e -> f

# a -> b -> d -> e -> f

def print_list(head):
    if head == None:
        return
    current = head
    print(current.val)
    print_list(current.next)


def remove_node(head, target_val):
    prev = None
    current = head

    if head.val == target_val:
        return head.next

    while current is not None:
        prev = current
        current = current.next
        if current.val == target_val:
            prev.next = current.next
            return head


print_list(remove_node(a, "f"))
