#Реализовать функцию my_func(), которая принимает три позиционных аргумента и возвращает сумму наибольших двух аргументов.
def my_func():
    num_1 = int(input("Укажите первое число: "))
    num_2 = int(input("Укажите второе число: "))
    num_3 = int(input("Укажите третье число: "))
    num_list = [num_1, num_2, num_3]
    min_num = min(num_list)
    num_list.remove(min_num)
    return sum(num_list)


print(f'Сумма максимальных чисел равна: {my_func()}')
