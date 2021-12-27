from json import load

from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView

from cartapp.models import Cart
from .models import Shoes, Clothes, Toy, Category

# Create your views here.
from mainapp.models import Shoes, Clothes, Toy


def read(content):
    with open(f"mainapp/templates/json/{content}.json", "r", encoding='UTF-8') as read_file:
        return load(read_file)


links_menu = read('links_menu')
header_menu = read('header_menu')


# links_menu = [
#     {'href': 'main:products_all', 'name': 'Все товары'},
#     {'href': 'main:products_recommendation', 'name': 'Рекомендуем'},
#     {'href': 'main:products_action', 'name': 'Акции'},
#     {'href': 'main:products_sale', 'name': 'Распродажа'},
# ]

# header_menu = [
#     {'href': 'main:index', 'name': 'ДОМОЙ'},
#     {'href': 'main:products', 'name': 'НАШИ ТОВАРЫ'},
#     {'href': 'main:about', 'name': 'О НАС'},
#     {'href': 'main:contact', 'name': 'НАШИ КОНТАКТЫ'},
# ]


def main(request, pk=None):  # , pk=None

    shoes = Shoes.objects.all()
    clothes = Clothes.objects.all()
    toys = Toy.objects.all()
    products = shoes.union(clothes)

    content = {
        'title': 'Главная',
        'header_menu': header_menu,
        'shoes': shoes,
        'clothes': clothes,
        'toys': toys,
        'products': products

    }
    return render(request, 'mainapp/index.html', content)


def product(request, pk=None):  # , pk=None

    links_menu_category = Category.objects.all()

    links_menu_shoes = Shoes.objects.all()
    links_menu_clothes = Clothes.objects.all()
    links_menu_toys = Toy.objects.all()
    links_menu_product = links_menu_shoes.union(links_menu_clothes)  #, links_menu_toys
    # links_menu_product = Shoes.objects.raw('SELECT * FROM Shoes UNION SELECT * FROM Clothes UNION SELECT * FROM Toy')


    if pk is not None:

        cart = []
        if request.user.is_authenticated:
            cart = Cart.objects.filter(user=request.user)

        if pk == 0:
            products = links_menu_product.order_by('price')#
            category = {'name': 'Все'}
        else:
            category = get_object_or_404(links_menu_category, pk=pk)
            products = links_menu_product.filter(category__pk=pk).order_by('price')#

        content = {
            'title': 'Товары',
            'links_menu': links_menu,
            'links_menu_product': links_menu_category,
            'header_menu': header_menu,
            'category': category,
            'products': products,
            'cart': cart
        }

        return render(request, 'mainapp/products_list.html', content)

    same_products = links_menu_product#[3:5]

    content = {
        'title': 'Товары',
        'links_menu': links_menu,
        'header_menu': header_menu,
        'links_menu_product': links_menu_category,
        'same_products': same_products
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
