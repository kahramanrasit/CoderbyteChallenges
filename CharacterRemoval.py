def CharacterRemoval(strArr):

  word = strArr[0]
  text = strArr[1]
  text = text.split(',')

  for i in range(len(text) - 1):
    for k in range(len(text) - i - 1):
      if len(text[k]) < len(text[k + 1]):
        temp = text[k] 
        text[k] = text[k + 1]
        text[k + 1] = temp
  
  

  for e in text:
    text_l = list(e)
    word_l = list(word)
    cnt = 0
    while len(word_l) != 0 and len(text_l) != 0:
      if text_l[0] == word_l[0]:
        text_l.pop(0)
        word_l.pop(0)
      elif text_l[0] != word_l[0]:
        word_l.pop(0)
        cnt += 1
    if len(text_l) == 0 and len(word_l) == 0:
      return cnt    
    elif len(text_l) == 0 and len(word_l) != 0:
      return cnt + len(word_l)
  return -1

  



  

# keep this function call here 
print(CharacterRemoval(input()))
