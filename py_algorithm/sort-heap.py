

def heapify(arr, n , i):
  largest = i
  l = 2 * i + 1     # left = 2*i + 1
  r = 2 * i + 2 
 
  if l < n and arr[largest] < arr[l]:
    largest = l
  if r < n and arr[largest] < arr[r]:
    largest = r
  if largest != i:
    arr[i],arr[largest] = arr[largest],arr[i]  # swap
    heapify(arr, n, largest)

def heap_sort(lst):
  n = len(lst)
  for i in range(n/2, -1, -1):
    heapify(lst, n, i)

  for i in range(n-1, 0, -1):
    lst[i], lst[0] = lst[0], lst[i]   # swap
    heapify(lst, i, 0)


l=[9,2,1,7,6,8,0,5,12,3,4]
heap_sort(l)
print l