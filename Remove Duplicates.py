arr=[1,1,2,2,2,3,4,5,5,5]
slow=0
for fast in range(1,len(arr)):
  if arr[slow]!=arr[fast]:
    slow+=1
    arr[slow]=arr[fast]
print(arr)
print(arr[:slow+1])
