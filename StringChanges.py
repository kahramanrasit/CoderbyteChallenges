def StringChanges(strParam):
  s = list(strParam)
  ret = []
  flag = False
  for i in range(len(s)):
    if flag == True:
      flag = False
      continue
    if s[i] == 'M':
      if len(ret) == 0:
        continue
      else:
        ret.append(ret[-1])
    elif s[i] == 'N':
      if i == len(s) - 1:
        continue
      else:
        flag = True
    else:
      ret.append(s[i])

    strParam = ''.join(ret)


  
  return strParam

# keep this function call here 
print(StringChanges(input()))
