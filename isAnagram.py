

# def isAnagram(word:str):
#   pos=1
#   vogal=0
#   inverted=''
#   word = word.lower()
#   for letter in word:
#     print(letter, f'{pos}')
#     if (letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u'):  

#       vogal+=1  
#     pos+=1    
#   for i in word:
#       inverted= i + inverted

    
#   print(f'A quantidade de vogais em {word} é: {vogal}')
#   print(f'A palavra invertida fica: {inverted}')



# isAnagram('Corno')    

# def anagram(word1:str,word2:str):
#   if(len(word1)!=len(word2)):
#     return False
#   contador = {}

#   for letra in word1:
#     if(letra not in contador):
#       contador[letra] = 1
#     else:
#       contador[letra] +=1
#   for letra in word2:
#     if(letra in contador):
#       contador[letra] -= 1
#       if contador[letra] < 0:
#         return False
#     else:
#       return False
  
#   return True  

# print(anagram('amor','roma'))

def repeatWord(word1:str):
  wordLetters={}
  for letter in word1:
    if letter not in wordLetters:
      wordLetters[letter] = 1
    else:
      wordLetters[letter] +=1

  print(wordLetters)    
  for letter in word1:
    if wordLetters[letter]<2:
      print(f'Letter: ({letter}) its the first one to not repeat')

repeatWord('amapa')