def threeSum(self,nums:list[int],target:int):
  pairs= []
  
  for i in range(len(nums)):
    for j in range(i+1, len(nums)):
      for k in range(j+1,len(nums)):
        if nums[i]+nums[j]+nums[k] == target:
          pairs.append((i,j,k)) 
          
      
        
        
  return pairs

print(threeSum(1,[2,3,3],8))


