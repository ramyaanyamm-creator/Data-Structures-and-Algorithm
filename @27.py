nums=[1,3,2,4,5,5,2,5,6,3,5]
val=3
slow=0
for fast in range(len(nums)):
  if nums[fast]!=val:
    nums[slow]=nums[fast]
    slow+=1
print(nums[:9])
