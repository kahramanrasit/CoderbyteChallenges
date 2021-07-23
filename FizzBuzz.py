def FizzBuzz(num):

  l = [str(i) for i in range(1, num + 1)]
 
  for i in range(1, len(l) + 1):
    if (i % 3 == 0) and (i % 5 == 0):
      l[i - 1] = "FizzBuzz"
    elif i % 3 == 0:
      l[i - 1] = "Fizz"
    elif i % 5 == 0:
      l[i - 1] = "Buzz"


  return ' '.join(l)

# keep this function call here 
print(FizzBuzz(input()))
