# https://www.structy.net/problems/premium/reverse-string-recursive

def reverse_string(s):
  if len(s) == 0:
    return ''
  return reverse_string(s[1:]) + s[0]

print(reverse_string("hello"))