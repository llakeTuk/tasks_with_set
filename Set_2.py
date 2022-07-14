from collections.abc import Hashable

def list_to_set(input_list):
  st = {elem for elem in input_list if isinstance(elem, Hashable)}
  print(st)
y = 'y'
while y == 'y':
  input_data = input('enter list of elements, using comma: ').split(',')
  list_to_set(input_data))
  y = input('restart?(y/n): ')
print('goodbye')
