capitals = {'USA': 'WashingtonDC', 'France': 'Paris', 'UK': 'London', 'India': 'New Delhi'}
print(capitals.values())
print(capitals.keys())
print(capitals)
for i in capitals.keys():
  print(i,capitals[i])
  print('USA' in capitals)
capitals['Germany'] = 'Berlin'
del capitals['Germany']
capitals['France'] = 'NotParis'