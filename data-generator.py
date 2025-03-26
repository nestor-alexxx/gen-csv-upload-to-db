import pandas as pd
import random
from random import randint 
import string 

goods_dict = {"Бытовая химия": {"Fairy моющее средство": 150, 
                                "Comet чистящее средство": 170,
                                "Крот средство от засоров": 120,
                                "AOS моющее средство": 130}, 
              "Текстиль": {"Наволочка квадратная": 600,
                           "Наволочка прямоугольная": 650,
                           "Простынь 1": 1200,
                           "Простынь 1.5": 1500,
                           "Простынь 2": 2100,
                           "Пододеяльник 1": 1500,
                           "Пододеяльник 1.5": 1700,
                           "Пододеяльник 2": 2200,
                           "Полотенце мал": 500,
                           "Полотенце бол": 1100},
              "Посуда": {"Тарелка мал": 150,
                         "Тарелка бол": 220,
                         "Набор блюдец": 470,
                         "Стакан синий": 220,
                         "Стакан черный": 220,
                         "Набор кастрюль": 3500}, 
              "Инструменты": {"Отвертка + мал": 80,
                              "Отвертка + бол": 130,
                              "Отвертка - мал": 80,
                              "Отвертка - бол": 130,
                              "Плоскогубцы": 320,
                              "Бокорезы": 300}, 
              "Канцтовары": {"Ручка синяя": 50,
                             "Ручка зеленая": 50,
                             "Ручка красная": 50,
                             "Бумага 100 листов": 600,
                             "Канцелярский нож": 80,
                             "Малярный скотч": 60}}

goods_df = pd.DataFrame(columns=['category', 'good', 'price'])
for cat in goods_dict.keys():
    for good in goods_dict[cat]:
        new_row = {'category': cat, 'good': good, 'price': goods_dict[cat][good]}
        goods_df.loc[len(goods_df)] = new_row

goods_df['good_id'] = [x for x in range(1, len(goods_df)+1)]
goods_df = goods_df[['good_id', 'category', 'good', 'price']]

# продуктовая матрица готова


shops_and_cash = ['11', '12', '13', '14', '21', '31', '32', '41']

# готовим функции
def generate_invoice_id(sh_c):
    characters = string.ascii_letters + string.digits
    return sh_c + ''.join(random.choice(characters) for _ in range(8))

def invoice_multiplier(lst):
    result = []
    for el in lst:
        result.extend([el] * randint(1, 2))
    return result

def generate_good_cat_price(sales_len):
    good_cat_price = [goods_df.iloc[randint(0, len(goods_df)-1)]]

    for i in range(sales_len-1):
        row_num = randint(0, len(goods_df)-1)
        new_ser = goods_df.iloc[row_num]

        if not new_ser.equals(good_cat_price[i]):
            good_cat_price.append(new_ser)
        else:
            try:
                good_cat_price.append(goods_df.iloc[row_num+1])
            except:
                good_cat_price.append(goods_df.iloc[row_num-1])


    goods_list, cat_list, price_list = [], [], []

    for ser in good_cat_price:
        goods_list.append(ser['good'])
        cat_list.append(ser['category'])
        price_list.append(ser['price'])

    return {'good': goods_list, 'cat': cat_list, 'price': price_list}

# создаем временные дф и сохраняем данных из них в файлы
for el in shops_and_cash:
    sales = pd.DataFrame(columns=['doc_id', 'item', 'category', 'amount', 'price', 'discount'])
    unique_invoices = [generate_invoice_id(el) for _ in range(randint(500, 800))]

    sales['doc_id'] = invoice_multiplier(unique_invoices)
    good_cat_price = generate_good_cat_price(len(sales))
    sales['item'] = good_cat_price['good']
    sales['category'] = good_cat_price['cat']
    sales['price'] = good_cat_price['price']
    sales['amount'] = [randint(1, 5) for _ in range(len(sales))]
    sales['discount'] = [random.choices([0, randint(1, 15)], weights=[65, 35])[0] for _ in range(len(sales))]

    sales.to_csv(f'data/{el[0]}_{el[1]}.csv')

# данные сгенерированы и помещены в соответствующие csv-файлы