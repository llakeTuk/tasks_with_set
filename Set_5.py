
def set_generation(lst):
  list_index = 0
  while list_index < len(lst):
    count_number = lst.count(lst[list_index])
    if count_number > 1:
      lst[list_index] = str(lst[list_index]) * count_number
    list_index += 1
  return set(lst)
y = 'y'
while y == 'y':
  input_list = list(map(int, input('enter list of integer numbers, using comma: ').split(',')))
  print(set_generation(input_list))
  y = input('restart?(y/n): ')