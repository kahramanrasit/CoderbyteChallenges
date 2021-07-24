def StringCalculate(strParam):
  
  l = list(strParam)

  for i in range(len(l) - 1):
    if l[i + 1] == '(' and l[i] != '(': 
       if l[i] != '*' and l[i] != '/' and l[i] != '+' and l[i] != '-':
        l.insert(i + 1, '*')

  strParam = ''.join(l)
  
  return int(eval(strParam))

# keep this function call here 
print(StringCalculate(input()))

#((-2*0-9*0)*0)+5**6
