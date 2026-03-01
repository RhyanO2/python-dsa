def wordDEFINITION(word:str):
  pos=1
  vogal=0
  inverted=''
  word = word.lower()
  for letter in word:
    print(letter, f'{pos}')
    if (letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u'):  

      vogal+=1  
    pos+=1    
  for i in word:
      inverted= i + inverted

    
  print(f'A quantidade de vogais em {word} é: {vogal}')
  print(f'A palavra invertida fica: {inverted}')



wordDEFINITION('oioi')    