my_list = [1, 3, '32', 3.4, True]

del my_list[2]
print(my_list)
print(len(my_list))
my_list.sort(reverse=True)  # Сортировка списка в обратном порядке
print(my_list)

my_list2 = [5, 1]
my_list.extend(my_list2)  # Расширение списка за счет другого списка

print(my_list)
