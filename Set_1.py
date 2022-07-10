def to_set(input_string):
  st = set(input_string)
  return st, len(st)
y = 'y'
while y == 'y':
  input_data = input('enter string: ')
  print(to_set(input_data))
  print(*to_set(input_data))
  y = input('restart?(y/n): ')