time = int(input("Введите число от 1 до 86 400: "))
while time > 86400 or time < 0:
    time = int(input("Давай ещё раз, введи число от 1 до 86 400: "))
hh = time // 3600
mm = time % 3600 // 60
ss = time % 3600 % 60

print(f"{time} секунд - это {hh:>02d}:{mm:>02d}:{ss:>02d}")
