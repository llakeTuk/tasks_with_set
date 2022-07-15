
def super_set(set_1, set_2):
  if set_1 > set_2:
    print(f'{set_1} is super set')
  elif set_2 > set_1:
    print(f'{set_2} is super set')
  elif set_1 == set_2:
    print('sets are equal')
  else:
    print('supersets not found')
y = 'y'
while y == 'y':
  input_set_1 = set(input('enter set 1 of elements, using comma: ').split(','))
  input_set_2 = set(input('enter set 2 of elements, using comma: ').split(','))
  super_set(input_set_1, input_set_2)
  y = input('restart?(y/n): ')