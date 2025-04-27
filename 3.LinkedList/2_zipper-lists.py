# def zipper_lists(head_1, head_2):
#   current_1 = head_1
#   current_2 = head_2
#   count = 0
#   while current_1 is not None and current_2 is not None:
#     if count % 2 == 0:
#       temp_1 = current_1.next
#       current_1.next = current_2
#       current_1 = temp_1
#     if count % 2 != 0:
#       temp_2 = current_2.next
#       current_2.next = current_1
#       current_2 = temp_2
#     count += 1
#
#   return head_1

# recursion algo

def zipper_lists(head_1, head_2):
  if head_1 is None and head_2 is None:
    return None
  if head_1 is None:
    return head_2
  if head_2 is None:
    return head_1
  next_1 = head_1.next
  next_2 = head_2.next
  head_1.next = head_2
  head_2.next = zipper_lists(next_1, next_2)
  return head_1



def linked_list_values(head):
  values = []
  current = head
  while current is not None:
    values.append(current.val)
    current = current.next
  return values


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

x = Node("x")
y = Node("y")
z = Node("z")
x.next = y
y.next = z
# x -> y -> z



print(" a -> x -> b -> y -> c -> z -> d -> e -> f")
print(linked_list_values(zipper_lists(a, x)))

