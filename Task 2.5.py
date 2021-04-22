#Можно еще через цикл, но не успел написать
my_list = [7, 5, 3, 3, 2]
user_number = int(input('Введите число для последовательности:'))
my_list.append(user_number)
my_list.sort(reverse=True)
print(my_list)