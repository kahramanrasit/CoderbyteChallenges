def StringCalculate(strParam):

 # "(4/2)(3-1)" the output was incorrect. The correct output is 4

  # "7-4-1+8(3)/2
  
  s = list(strParam)
  res = []
  for i in range(len(s)):
    if i != len(s) -1:
      if s[i + 1] == '(' and s[i] != '(': 
        if s[i] == '*' or s[i] == '/' or s[i] == '-' or s[i] == '+':
          pass
        else:
          s.insert(i + 1,'*')

  strParam = ''.join(s)
  
  return int(eval(strParam))

# keep this function call here 
print(StringCalculate(input()))

#((-2*0-9*0)*0)+5**6
