# 1.	Реализуйте алгоритм перемешивания списка.

some_list = ['school', 'work', 'teacher', 'sky', 'sea', 'forest', 'people', 'love', 'children']
new_list = []

import random 
for i in range(len(some_list)):
    j = random.randint(0, len(some_list)-1)
    new_list.append(some_list[j])
    some_list.pop(j)
    

print(new_list)