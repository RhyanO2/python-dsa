# def stringCompression(word:str):
#   stringDict = {}
#   compressedStr = ''
#   for letter in word:
#     if letter not in stringDict:
#       stringDict[letter] = 1
#     else:
#       stringDict[letter] +=1
#   for i in stringDict:
    
#     compressedStr+=(f"{i}{stringDict[i]} ")
#   return compressedStr


# def stringCompression(word:str):
#   if not word: return ''
#   currentLetter = word[0]
#   count = 1
#   compressedStr = ''
#   for letter in range(1, len(word)):
#     if (word[letter] == currentLetter):
#       count+1
   
  
def stringCompression(word: str):
    if not word:
        return ''
    
    compressedStr = ''
    current_letter = word[0]
    count = 1
    
    for i in range(1, len(word)):
        if word[i] == current_letter:
            count += 1
        else:
            compressedStr += f"{current_letter}{count}"
            current_letter = word[i]
            count = 1
    
   
    compressedStr += f"{current_letter}{count}"
    
    return compressedStr


print(stringCompression('abaa'))