def quicksort(nums, left, right):
  if i >= j:
    return nums
  i = left;j = right;key = nums[i]

  while i < j:
    while i < j and nums[j] >= key:
      j-=1
    nums[i] = nums[j]
    while i < j and nums[i] <= key:
      i +=1
    nums[j] = nums[i]
  nums[i] = key 

  quicksort(nums, left, i-1)
  quicksort(nums, i+1, right)
  
  return nums

arr =[6,2,3,1,9,7,4] 
print quicksort(arr, 0, len(arr)-1)