my_list = [2, 'text', 1+2j, 45.3, None, True, ('i','j'), {'1': 'a', '2':'b'},[-4,-3,-2]]
for el in my_list:
    print(f'{el} - это {type(el)}', end="\n")
