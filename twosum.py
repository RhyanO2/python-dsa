

def twoSum(self,nums:list[int],target:int):
  pairs= []
  
  for i in range(len(nums)):
    for j in range(i+1, len(nums)):
      if nums[i]+nums[j] == target:
        pairs.append(i) 
        pairs.append(j)
      
        
        
  return pairs

print(twoSum(1,[1,3,5,2,3,4,2,3,4,3,2,4],8))


