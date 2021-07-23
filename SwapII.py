def SwapII(strParam):
#"123gg))((" the output was incorrect. The correct output is 123GG))((
  s = strParam.split()

  for i in range(len(s)):
    if s[i].isalpha():
      s[i] = s[i].swapcase()
      continue
    idx = 0
    l = list(s[i])
    flag = False
    for k in range(len(l)):
      if l[k].isdigit() and flag == False and k != len(l) - 1 and not l[k + 1].isdigit():
        idx = k
        flag = True
      elif l[k].isdigit() and flag == True:
        t = l[idx]
        l[idx] = l[k]
        l[k] = t
      

      if not l[k].isalnum() and flag == True:
        flag = False
        idx = None

    s[i] = ''.join(l)
    s[i] = s[i].swapcase()

  strParam = ' '.join(s)
 
  return strParam

# keep this function call here 
print(SwapII(input()))
