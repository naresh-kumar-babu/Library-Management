def quicksort(a,i,j, key):
  if len(a)==1:
    return a
  if i<j:
    d = partition(a,i,j, key)
    quicksort(a,i,d-1, key)
    quicksort(a,d+1,j, key)

def partition(a,i,j, key):
  pivot = j
  j-=1
  while i<j:
    while str(getattr(a[i], key)).lower() < str(getattr(a[pivot], key)).lower():
      i+=1
    while str(getattr(a[j], key)).lower() > str(getattr(a[pivot], key)).lower():
      j-=1
    if i<j:
      a[i],a[j]=a[j],a[i]
  a[i],a[pivot]=a[pivot],a[i]
  return i

def qSort(books, key):
  quicksort(books, 0, len(books)-1, key)
