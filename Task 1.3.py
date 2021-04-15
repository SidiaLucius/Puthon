user_number = int(input("Введите произвольное целое число: "))
con_num = int(len(str(user_number)))
sec_num = user_number * (10 ** con_num) + user_number
thr_num = user_number * 10 ** (2*con_num) + sec_num
print(f"Сумма числа {user_number} равна {user_number} + {sec_num} + {thr_num} = {user_number+sec_num+thr_num}))")