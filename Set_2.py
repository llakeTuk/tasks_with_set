from collections.abc import Hashable

def list_to_set(input_list):
  st = {element for element in input_list if isinstance(element, Hashable)}
  print(st)
y = 'y'
while y == 'y':
  input_data = input('enter list of elements, using comma: ').split(',')
  list_to_set(input_data))
  y = input('restart?(y/n): ')
