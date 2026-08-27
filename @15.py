class Solution(object):
    def threeSum(self, nums)
        nums.sort()
        total=[]

        for i in range(len(nums)):
            left=i+1
            right=len(nums)-1
            while left<right:
                sum=nums[i]+nums[left]+nums[right]
                if sum>0:
                    right-=1
                elif sum<0:
                    left+=1
                else:
                    total.append([nums[i], nums[left], nums[right]])
        return total
        
