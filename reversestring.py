

def reverseStr(str:str):
  counter = len(str)-1
  arrStr= []
  reverseWord = ''
  for i in str:
    arrStr.insert(counter,i)
    while counter>0:
      counter-=1
  for j in arrStr:
    reverseWord += j
    
  return reverseWord  


print(reverseStr('papo'))