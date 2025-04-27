# https://www.structy.net/problems/linked-list-values

class Node:
  def __init__(self, val):
    self.val = val
    self.next = None


a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

a.next = b
b.next = c
c.next = d


def fill_values(head, values):
  if head is None:
    return
  values.append(head.val)
  fill_values(head.next, values)


def linked_list_values(head):
  values = []
  fill_values(head, values)
  return values

print(linked_list_values(a))


# time complexity is : O(n^2)
# def linked_list_values(head):
#   if head is None:
#     return  []
#
#   return [head.val] + linked_list_values(head.next)
#
# print(linked_list_values(a))





# def linked_list_values(head):
#   values = []
#   _linked_list_values(head, values)
#   return values
#
# def _linked_list_values(head, values):
#   if head is None:
#     return
#   values.append(head.val)
#   _linked_list_values(head.next, values)


# linked_list_values(a)
