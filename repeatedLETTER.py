def repeatWord(word1:str):
  wordLetters={}
  for letter in word1:
    if letter not in wordLetters:
      wordLetters[letter] = 1
    else:
      wordLetters[letter] +=1
  repeated= []

  for letter in word1:
    if wordLetters[letter]==1:
      repeated.append(letter)

  return repeated

# print(repeatWord('amapa'))

# def repeatWord(word1:str):
#   wordLetters={}
#   for letter in word1:
#     if letter not in wordLetters:
#       wordLetters[letter] = 1
#     else:
#       wordLetters[letter] +=1
#   arrayWord= []
#   repeated=[]
#   for letter in word1:
#     arrayWord.append(letter)
#     print(arrayWord)
#   if(len(arrayWord)==len(word1)):
#     if wordLetters[letter]==1:
#     return arrayWord[letter]

    # if wordLetters[letter]==1:
    #   repeated.append(letter)

  # return repeated

# print(repeatWord('amapa'))

def repeatWord(word1:str):
  wordLetters={}
  for letter in word1:
    if letter not in wordLetters:
      wordLetters[letter] = 1
    else:
      wordLetters[letter] +=1
  repeated= []

  for letter in word1:
    if wordLetters[letter]==1:
      repeated.append(letter)

    return repeated

print(repeatWord('amapa'))
