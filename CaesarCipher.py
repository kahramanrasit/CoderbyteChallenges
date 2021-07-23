def CaesarCipher(strParam,num):


  s = list(strParam)
  
  for i in range(len(s)):
    if s[i].isalpha():
      if not chr(ord(s[i]) + num).isalpha():
        s[i] = chr(ord(s[i]) + num - 26)
      else:
        s[i] = chr(ord(s[i]) + num)
  
  strParam = ''.join(s)

  return strParam

# keep this function call here 
print(CaesarCipher(input()))
