arr=[2,5,7,8,13,23]
i=0
j=len(arr)-1
target=15
while(i<j):
  sum=arr[i]+arr[j]
  if sum>target:
    j-=1
  elif sum<target:
    i+=1
  else:
    print(arr[i],arr[j])
    break
