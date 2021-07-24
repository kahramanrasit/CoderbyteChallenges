def StringChanges(strParam):
  l = list(strParam)
  res = [] # Sonucun tutulacaÄÄ± boÅ bir list (result)

  flag = False
  for i in range(len(l)):

    """ flag'in true olmasÄ± N'den bir sonraki elemanÄ± gÃ¶sterdiÄi
     iÃ§in res'e ekleme iÅlemi yapÄ±lmayacaÄÄ±nÄ± belirtir.   """ 
    if flag == True: 
      flag = False
      continue

    if l[i] == 'M':  # M 'i gÃ¶stermesi durumunda 
      if len(res) == 0:  # Dizinin ilk elemanÄ± ise hiÃ§bir Åey yapma
        continue
      else: # Dizinin ilk elemanÄ± deÄilse bir Ã¶nceki elemanÄ± res'e ekle
        res.append(res[-1])
        continue

    if l[i] == 'N':  # N 'i gÃ¶stermesi durumu
      if i == len(l) - 1: # EÄer son elemansa hiÃ§bir Åey yapma 
        continue
      else: # Son eleman deÄilse flag'Ä± True yap
        flag = True 
        continue

    res.append(l[i]) # EÄer yukarÄ±da hiÃ§bir iÅlem yapÄ±lmadÄ±ysa elemanÄ± res' e ekle.
    
  strParam = ''.join(res)

 
  return strParam

# keep this function call here 
print(StringChanges(input()))
