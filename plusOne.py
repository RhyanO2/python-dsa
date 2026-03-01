class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        list=[]
        for i in range (len(digits)):
            if(i == len(digits)-1):    
                list.append(digits[i]+1)
                if list[0] == 10:
                    for j in str(list[i]):
                        list.append(int(j))
                    list.pop(i)


                return list
            list.append(digits[i])

            
        return list        
