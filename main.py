slv =(input('Введіть слово(без CapsLock):'))
count = {}
for s in slv:
  if s in count:
    count[s] += 1
  else:
    count[s] = 1
print('В слові', '"', slv, '"', 'повторюються:')
for key in count:
  if count[key] > 1:
    print(key, end=" "), count[key]
