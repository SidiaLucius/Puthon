ser_phrase = input("Введите любимую крылатую фразу из фильмов: ")
ser_phrases = ser_phrase.split()
for ind, el in enumerate(ser_phrases, 1):
    print(f'{ind} {el[:10]}', end='\n')