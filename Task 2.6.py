ans_cl = 'да'
pr_nu_li = []
l_pr_name = []
l_pr_price = []
l_pr_qu = []
l_pr_par = []
while ans_cl == 'да':
    pr_name = input('Введите название продукта: ')
    pr_price = int(input('Введите цену товара: '))
    pr_qu = int(input('Введите кол-во товара: '))
    pr_par = input('Введите единицу измерения товара(шт./кг.): ')
    pr_dic = {'Название товара': pr_name, 'Цена': pr_price, 'Количество товара': pr_qu, 'Единица измерения': pr_par}
    pr_nu_li.append(pr_dic)
    ans_cl = input('Ещё товары (да/нет)?: ')
for ind, el in enumerate(pr_nu_li, 1):
    print(f'{(ind, el)}', end='\n')
for dic in pr_nu_li:
    l_pr_name.extend(dic.get('Название товара'))
    l_pr_price.extend(str(dic.get('Цена')))
    l_pr_qu.extend(str(dic.get('Количество товара')))
    l_pr_par.extend(dic.get('Единица измерения'))
dic_4_an = {"Названия": l_pr_name, "Цены": l_pr_price, "Количества": l_pr_qu, "Виды е.и.": l_pr_par}
print(dic_4_an)