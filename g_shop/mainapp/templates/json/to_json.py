import json


links_menu = [
    {'href': 'products_all', 'name': 'Все товары'},
    {'href': 'products_recommendation', 'name': 'Рекомендуем'},
    {'href': 'products_action', 'name': 'Акции'},
    {'href': 'products_sale', 'name': 'Распродажа'},
]

header_menu = [
    {'href': 'index', 'name': 'ДОМОЙ'},
    {'href': 'products', 'name': 'НАШИ ТОВАРЫ'},
    {'href': 'about', 'name': 'О НАС'},
    {'href': 'contact', 'name': 'НАШИ КОНТАКТЫ'},
]


def write(content, name_file):
    with open(f"{name_file}.json", "w") as write_file:
        json.dump(content, write_file, indent=4, sort_keys=True)


# def read(content):
#     with open(f"{content}.json", "r", encoding='UTF-8') as read_file:
#         return json.load(read_file)


# write(links_menu, 'links_menu')
# write(header_menu, 'header_menu')
# print(read('links_menu'))
# print(read('header_menu'))
