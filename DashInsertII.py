def DashInsertII(num):
  if len(str(num)) < 2:
    return num

  num = list(str(num))
  l = []
  
  for i in range(len(num) - 1):
    
    if num[i] != '0' and num[i + 1] != '0':
      if int(num[i]) % 2 == 0 and int(num[i + 1]) % 2 == 0:
        l.append(num[i])
        l.append('*')
      elif int(num[i]) % 2 != 0 and int(num[i + 1]) % 2 != 0:
        l.append(num[i])
        l.append('-')
      else:
        l.append(num[i])
      if i == len(num) - 2:
        l.append(num[i + 1])
    else:
      l.append(num[i])
      if i == len(num) - 2:
        l.append(num[i + 1])
 
  num = ''.join(l)

  return num

# keep this function call here 
print(DashInsertII(input()))
