

def difference(set_1, set_2, set_3, symmetric = True):
  if symmetric:
    return set_1 ^ set_2 ^ set_3
  return set_1 - set_2 - set_3
y = 'y'
while y == 'y':
  print('enter 3 sets of elements, using comma')
  set_1 = set(input('enter 1 set: ').split(','))
  set_2 = set(input('enter 2 set: ').split(','))
  set_3 = set(input('enter 3 set: ').split(','))
  symm = input('symmetric difference?(y/n): ')
  if symm == 'y':
    print(difference(set_1, set_2, set_3, symmetric = True))
  elif symm == 'n':
    print(difference(set_1, set_2, set_3, symmetric = False))
  else:
    print('invalid symbol')
  y = input('restart?(y/n): ')