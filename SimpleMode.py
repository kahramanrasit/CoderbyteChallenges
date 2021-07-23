def SimpleMode(arr):
  
  l = []
  for e in arr:
    if e not in l:
      l.append(e)
  
  cnt = [0 for _ in l]
  

  for e in arr:
    cnt[l.index(e)] += 1

  
  if max(cnt) > 1:
    return l[cnt.index(max(cnt))]

  
  return -1

  

# keep this function call here 
print(SimpleMode(input()))
