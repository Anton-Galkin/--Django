from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.urls import reverse


User = get_user_model()


# def get_product_url(obj, viwename):
#     ct_model = obj.__class__._meta.model_name
#     return reverse(viwename, kwargs={'ct_model': ct_model, 'slug': obj.slug})


class Category(models.Model):
    name = models.CharField(primary_key=True, max_length=150, verbose_name='Категория', unique=True)
    descriptions = models.TextField(verbose_name='Описание', blank=True)
    slug = models.SlugField(unique=True)
    is_active = models.BooleanField(verbose_name='активна', default=True)

    def __str__(self):
        return self.name


class Product(models.Model):

    class Meta:
        abstract = True

    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)
    name = models.CharField(max_length=150, verbose_name='Наименование')
    image = models.ImageField(upload_to='product_images', blank=True)
    short_desc = models.CharField(max_length=150, verbose_name='Краткое описание', blank=True)
    description = models.TextField(verbose_name='Полное описание', blank=True)
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Цена', default=0)
    quantity = models.PositiveIntegerField(verbose_name='Количество на складе', default=0)

    def __str__(self):
        return f'{self.name} ({self.category.name})'


class Shoes(Product):
    brand_name = models.CharField(max_length=150, verbose_name='Бренд')
    size = models.CharField(max_length=2, verbose_name='Размер')
    gender = models.CharField(max_length=1, verbose_name='Пол')
    color = models.CharField(max_length=50, verbose_name='Цвет')

    def __str__(self):
        return f'{self.name}, {self.brand_name}, {self.size}'

    # def get_absolute_url(self):
    #     return get_product_url(self, 'product_detail')


class Clothes(Product):
    brand_name = models.CharField(max_length=150, verbose_name='Бренд')
    size = models.CharField(max_length=2, verbose_name='Размер')
    gender = models.CharField(max_length=1, verbose_name='Пол')
    color = models.CharField(max_length=50, verbose_name='Цвет')

    def __str__(self):
        return f'{self.name}, {self.brand_name}, {self.size}'

    # def get_absolute_url(self):
    #     return get_product_url(self, 'product_detail')


class Toy(Product):
    brand_name = models.CharField(max_length=150, verbose_name='Бренд')
    t_type = models.CharField(max_length=150, verbose_name='Тип игрушки')
    color = models.CharField(max_length=50, verbose_name='Цвет')

    def __str__(self):
        return f'{self.t_type}, {self.brand_name}, {self.name}'

    # def get_absolute_url(self):
    #     return get_product_url(self, 'product_detail')


class CartProduct(models.Model):
    user = models.ForeignKey('Customer', verbose_name='Покупатель', on_delete=models.CASCADE)
    cart = models.ForeignKey('Cart', verbose_name='Корзина', on_delete=models.CASCADE, related_name='related_products')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    quantity = models.PositiveIntegerField(default=1)
    final_price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Стоимость', default=0)

    def __str__(self):
        return f'Продукт {self.product.name}, количество: {self.quantity}, общая стоимость: {self.final_price}'


class Cart(models.Model):
    owner = models.ForeignKey('Customer', verbose_name='Владелец корзины', on_delete=models.CASCADE)
    products = models.ManyToManyField(CartProduct, blank=True, related_name='related_cart')
    total_products = models.PositiveIntegerField(default=0)
    final_price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Стоимость', default=0)

    def __str__(self):
        return f'Корзина: {self.owner}, id: {self.id}, Цена всего: {self.final_price}'


class Customer(models.Model):
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, verbose_name='Номер телефона')
    address = models.CharField(max_length=255, verbose_name='Адрес')

    def __str__(self):
        return f'Покупатель: {self.user.first_name} {self.user.last_name}'

