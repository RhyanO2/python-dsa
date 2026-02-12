def anagram(word1:str,word2:str):
  if(len(word1)!=len(word2)):
    return False
  contador = {}

  for letra in word1:
    if(letra not in contador):
      contador[letra] = 1
    else:
      contador[letra] +=1
  for letra in word2:
    if(letra in contador):
      contador[letra] -= 1
      if contador[letra] < 0:
        return False
    else:
      return False
  
  return True  

print(anagram('amor','roma'))