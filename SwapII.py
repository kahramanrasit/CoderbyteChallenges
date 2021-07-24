def SwapII(strParam):
 
  strParam = strParam.swapcase()
  word = strParam.split()
  res = []
  
  for e in word:
    l = list(e)
    idx = 0
    flag = False
    cnt = [i for i in l if i.isdigit()]
    if len(cnt) >= 3:
      res.append(''.join(l))
      continue
    else:
      for i in range(len(l)):
        if l[i].isdigit() and flag == False:
          idx = i
          flag = True
        elif not l[i].isalnum() and flag == True:
          flag = False
        elif l[i].isdigit() and flag == True:
          t = l[idx]
          l[idx] = l[i]
          l[i] = t

    res.append(''.join(l))
    

  strParam = ' '.join(res)
  
  return strParam
      
      
# keep this function call here 
print(SwapII(input()))
