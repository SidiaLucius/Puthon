dis_a = int(input('Растояние для первой тренировки: '))
dis_b = int(input('Итоговая дистинция: '))
if dis_b <= dis_a:
    print("Тебе не нужны тренировки!")
else:
    steps = 1
    next_step = dis_a * (1.1 ** steps)
    while dis_b >= next_step:
        next_step = dis_a * (1.1 ** steps)
        steps += 1
print(f'Через {steps} дня(ей).')