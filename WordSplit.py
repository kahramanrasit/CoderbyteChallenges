def isequal(syl, word): # fonksiyonda tüm dizinin elemanlarının kombinasyonları deneniyor.

  for i in range(len(syl) - 1):
    for j in range(i + 1, len(syl)):
      t = [syl[i], syl[j]]
      temp = ''.join(t)
      if temp == word:
        return ','.join(t)

  return -1


def WordSplit(strArr):

  word = strArr[0]
  syllable = strArr[1].split(',')

  t = isequal(syllable, word) # fonksiyon içerisinde tüm kombinasyonlar deneniyor.
  if t != -1:
    return t

  syllable = syllable[::-1] # dizi ters çeviriliyor 

  t = isequal(syllable, word) # tersten tüm kombinasyonlar deneniyor.
  if t != -1:
    return t

  return "not possible"



  

# keep this function call here 
print(WordSplit(input()))
