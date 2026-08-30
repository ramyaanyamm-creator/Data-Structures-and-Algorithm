nums=[1,-3,2,-5,4,6,-3,-7,8,9]
k=3
left=0
right=k
current_sum=sum(nums[left]:nums[right])
max_sum=current_sum
while right<len(nums):
  current_sum=current_sum-nums[left]+nums[right]
  left+=1
  right+=1
  if current_sum>max_sum:
    max_sum=current_sum

print(float(max_sum)/k)
