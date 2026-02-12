

def cpfValidator(cpf):
  if(len(cpf)==11):
    validator=10
    arr=[]
    salt=0
    acc=0
    secondDigitValidator= 11
    secondDigitAcc=0
    saltSecondDigit=0
    for i in cpf:
      
      arr.append(int(i))
      print(arr)
      
      if (len(arr)>9) and (len(arr)<11):
        acc+=validator*arr[salt]

        validatorAcc = acc

        print(validatorAcc)
        if (validatorAcc%11)<2:
          print(arr[9]==0)
        if (validatorAcc%11)>=2 or (validatorAcc%11)==2:
          print(arr[9],arr[9]== (11-validatorAcc%11))
          for j in arr:
            if(secondDigitValidator!=2):
              print(arr[saltSecondDigit])
              print(secondDigitValidator)
              secondDigitAcc+=(arr[saltSecondDigit] * secondDigitValidator)
              secondDigitValidator-=1
              saltSecondDigit+=1
              
              print(secondDigitAcc)          
      # if(len(arr)==9):
      #     acc+=validator*arr[salt]
      #     print(len(arr))
      #     print(acc)
      
      if((len(arr)<9) or len(arr)>9):
        # print(len(arr))
  
        acc+=validator*arr[salt]
        
        validator-=1

        
       

      salt+=1
      
      

      # if validator == 2:
      #   acc%11
      

  
  # print(arr)
  # print(acc)
cpfValidator('63117213333')