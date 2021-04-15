user_number = int(input("Введите произвольное целое положительное число: "))
while user_number <= 0:
    user_number = int(input("Давай ещё раз, целое положительное, это не сложно: "))
count_number = int(len(str(user_number)))
max_number = 0
while count_number > 0:
    number_pre = (user_number % 10 ** count_number) // 10 ** (count_number - 1)
    max_number = max(max_number, number_pre)
    count_number = count_number - 1

print(f'Наибольшая цифра - это {max_number}')