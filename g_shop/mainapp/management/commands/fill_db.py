from django.core.management.base import BaseCommand
from mainapp.models import Shoes, Toy, Clothes, Category
from django.contrib.auth.models import User
from authapp.models import ShopUser

import json, os


JSON_PATH = 'mainapp/json'


def load_from_json(f_name):
    with open(os.path.join(JSON_PATH, f_name + '.json'), 'r', encoding='UTF-8') as file:
        return json.load(file)


def add_product(products, table):
    # table.objects.all().delete()
    for product in products:
        category_name = product["fields"]["category"]
        # print(category_name)
        # Получаем категорию по имени
        _category = Category.objects.get(name=category_name)
        print(_category)
        # Заменяем название категории объектом
        product['category'] = _category
        new_product = table(**product)
        print(new_product)
        new_product.save()
        print(category_name, _category, new_product)


class Command(BaseCommand):
    def handle(self, *args, **options):
        # categories = load_from_json('categories')
        #
        # # ProductCategory.objects.all().delete()
        # for category in categories:
        #     new_category = Category(**category)
        #     new_category.save()

        # products = load_from_json('products')

        shoes = load_from_json('shoes')
        add_product(shoes, Shoes)

        clothes = load_from_json('clothes')
        add_product(clothes, Clothes)

        toys = load_from_json('toys')
        add_product(toys, Toy)


        # # Product.objects.all().delete()
        # for product in products:
        #     category_name = product["category"]
        #     # Получаем категорию по имени
        #     _category = Category.objects.get(name=category_name)
        #     # Заменяем название категории объектом
        #     product['category'] = _category
        #     new_product = Product(**product)
        #     new_product.save()

        # Создаем суперпользователя при помощи менеджера модели
        # super_user = ShopUser.objects.create_superuser('admin', '4qguns@gmail.com', 'admin', age=35)
