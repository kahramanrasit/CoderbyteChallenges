def WordSplit(strArr):
  word = strArr[0]
  syllable = strArr[1]
  syllable = syllable.split(',')

  for i in range(len(syllable) - 1):
    for j in range(i + 1, len(syllable)):
      temp = [syllable[i], syllable[j]]
      temp = ''.join(temp)
      if word == temp:
        temp = [syllable[i], syllable[j]]
        return ','.join(temp)

  syllable = syllable[::-1]

  for i in range(len(syllable) - 1):
    for j in range(i + 1, len(syllable)):
      temp = [syllable[i], syllable[j]]
      temp = ''.join(temp)
      if word == temp:
        temp = [syllable[i], syllable[j]]
        return ','.join(temp)

  return "not possible"



  

# keep this function call here 
print(WordSplit(input()))
