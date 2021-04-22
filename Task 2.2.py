user_list = input("Введите без пробелов и заяпятых элементы списка: ")
str_reverse = ''
symbols = list(user_list)
rev = 0
for el in range(len(user_list) // 2):
    symbols[rev], symbols[rev + 1] = symbols[rev + 1],  symbols[rev]
    rev += 2
str_reverse = ''.join(symbols)
print(str_reverse)