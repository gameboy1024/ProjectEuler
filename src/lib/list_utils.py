################################################################################
# Basic operations
################################################################################

def has_common_elements_from_sorted(a, b):
  if not len(a) or not len(b):
    return False
  p = 0
  q = 0
  while p < len(a) and q < len(b):
    if a[p] == b[q]:
      return True
    if a[p] < b[q]:
      p += 1
    else:
      q += 1
  return False