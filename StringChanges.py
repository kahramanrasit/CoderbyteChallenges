def StringChanges(strParam):
  l = list(strParam)
  res = [] # Sonucun tutulacağı boş bir list (result)

  for i in range(len(l)):

    flag = False
    
    """ flag'in true olması N'den bir sonraki elemanı gösterdiği
     için res'e ekleme işlemi yapılmayacağını belirtir.   """ 
    if flag == True: 
      flag = False
      continue

    if l[i] == 'M':  # M 'i göstermesi durumunda 
      if i == 0:  # Dizinin ilk elemanı ise hiçbir şey yapma
        continue
      else: # Dizinin ilk elemanı değilse bir önceki elemanı res'e ekle
        res.append(res[-1])
        continue

    if l[i] == 'N':  # N 'i göstermesi durumu
      if i == len(l) - 1: # Eğer son elemansa hiçbir şey yapma 
        continue
      else: # Son eleman değilse flag'ı True yap
        flag == True 
        continue

    res.append(l[i]) # Eğer yukarıda hiçbir işlem yapılmadıysa elemanı res' e ekle.
    
  strParam = ''.join(res)

 
  return strParam

# keep this function call here 
print(StringChanges(input()))
