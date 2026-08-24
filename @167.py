arr=[1,4,5,6,7]
i=0
j=len(arr)-1
target=7
while i<j:
  sum=arr[i]+arr[j]
  if sum<target:
    i+=1
  elif sum>target:
    j-=1
  else:
    print(arr[left],arr[right])
    break
