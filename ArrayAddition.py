def ArrayAddition(arr):

  if sum(arr) - max(arr) >= max(arr):
    return True
  else:
    return False
  
# keep this function call here 
print(ArrayAddition(input()))
