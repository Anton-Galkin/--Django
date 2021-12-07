import json

from django.shortcuts import render


# Create your views here.
from mainapp.models import Shoes, Clothes, Toy


def read(content):
    with open(f"mainapp/templates/json/{content}.json", "r", encoding='UTF-8') as read_file:
        return json.load(read_file)


links_menu = read('links_menu')
header_menu = read('header_menu')


# links_menu = [
#     {'href': 'products_all', 'name': 'Все товары'},
#     {'href': 'products_recommendation', 'name': 'Рекомендуем'},
#     {'href': 'products_action', 'name': 'Акции'},
#     {'href': 'products_sale', 'name': 'Распродажа'},
# ]
#
# header_menu = [
#     {'href': 'index', 'name': 'ДОМОЙ'},
#     {'href': 'products', 'name': 'НАШИ ТОВАРЫ'},
#     {'href': 'about', 'name': 'О НАС'},
#     {'href': 'contact', 'name': 'НАШИ КОНТАКТЫ'},
# ]

def main(request):

    shoes = Shoes.objects.all()
    clothes = Clothes.objects.all()
    toys = Toy.objects.all()

    content = {
        'title': 'Главная',
        'header_menu': header_menu,
        'shoes': shoes,
        'clothes': clothes,
        'toys': toys

    }
    return render(request, 'mainapp/index.html', content)


def product(request):
    content = {
        'title': 'Товары',
        'links_menu': links_menu,
        'header_menu': header_menu,
    }
    return render(request, 'mainapp/products.html', content)


def contact(request):
    content = {
        'title': 'Контакты',
        'header_menu': header_menu,
    }
    return render(request, 'mainapp/contact.html', content)


def about(request):
    content = {
        'title': 'О нас',
        'header_menu': header_menu,
    }
    return render(request, 'mainapp/about.html', content)


# def context(request):
#     content = {
#         'title': 'Магазин',
#         'header': 'Добро пожаловать на сайт',
#         'username': 'Галкин Антон',
#         'products': [
#             {'name': 'Шапки'},
#         ]
#     }
#     return render(request, 'mainapp/about.html')
