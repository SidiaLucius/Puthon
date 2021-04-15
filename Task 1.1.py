name = "Злобникус"
iq_lvl = 1
evil_lvl = 0.5
pls_level = "Да"
name = input("Ввведите своё имя: ")
iq_lvl = int(input("Введите чилсо от 1 до 100: "))

while iq_lvl > 100 or iq_lvl < 0:
    iq_lvl = int(input("Ещё раз! Чилсо от 1 до 100: "))

evil_lvl = float(input("Введите десятичное число от 0 до 1 (через точку): "))

while evil_lvl > 1 or evil_lvl < 0:
    evil_lvl = int(input("Ещё раз! Чилсо от 0 до 1: "))

pls_level = input("Понравился ли тест? (Да/Нет): ")

while pls_level != "Да" and pls_level != "да":
    pls_level = input('Ну может быть всё-таки "Да"?: ')

print(f"""Ваше злобное имя - {name}никус, 
Ваш IQ составляет - {iq_lvl}, 
Уровень озлобленности - {evil_lvl * 100}%, 
Понравился ли тест - {pls_level}""")