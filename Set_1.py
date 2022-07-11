def to_set(input_str):
  st = set(input_str)
  return st, len(st)
y = 'y'
while y == 'y':
  input_data = input('enter string: ')
  print(to_set(input_data))
  print(*to_set(input_data))
  y = input('restart?(y/n): ')
