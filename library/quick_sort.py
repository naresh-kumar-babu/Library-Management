def quicksort(a,i,j):
  if len(a)==1:
    return a
  if i<j:
    d = partition(a,i,j)
    quicksort(a,i,d-1)
    quicksort(a,d+1,j)

def partition(a,i,j):
  pivot = j
  j-=1
  while i<j:
    while a[i]['ISBN'].lower()<a[pivot]['ISBN'].lower():
      i+=1
    while a[j]['ISBN'].lower()>a[pivot]['ISBN'].lower():
      j-=1
    if i<j:
      a[i],a[j]=a[j],a[i]
  a[i],a[pivot]=a[pivot],a[i]
  return i

a = []
for i in range(int(input("Enter the no. of books:"))):
  l = input().split(",")
  a.append({'Book-Name:':l[0].strip(),'Author':l[1].strip(),'ISBN':l[2].strip()})
quicksort(a,0,len(a)-1)
print(a)