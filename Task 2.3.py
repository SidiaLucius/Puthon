list_w = [1, 2, 12]
list_sp = [3, 4, 5]
list_sum = [6, 7, 8]
list_aut = [9, 10, 11]
my_season = {'Зимний': list_w, "Весенний": list_sp, "Летний": list_sum, "Осенний": list_aut}
my_month = ['Декабрь','Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь']
cl_month = int(input(f"Введи номер месяца (от 1 до 12): "))
while cl_month > 12 or cl_month <= 0:
    cl_month = int(input("Введи номер месяца (от 1 до 12): "))
for key_1 in my_season.keys():
    if cl_month in my_season[key_1]:
        print(f' {my_month[cl_month % 12]} это {key_1} месяц')