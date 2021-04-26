#Реализовать функцию int_func(), принимающую слова из маленьких латинских букв и возвращающую их же, но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
def int_func():
    user_text = input("Введите обрабатываемый текст: ")
    return user_text.title()


print(int_func())
