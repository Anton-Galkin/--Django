from django.urls import path


# from .views import ProductDetailView
from .views import *
# import mainapp.views as mainapp


app_name = 'mainapp'


urlpatterns = [

    path('', main, name='index'),
    path('contact/', contact, name='contact'),
    path('about/', about, name='about'),
    path('products/', product, name='products'),

    path('products_all', product, name='products_all'),
    path('products_recommendation', product, name='products_recommendation'),
    path('products_action', product, name='products_action'),
    path('products_sale', product, name='products_sale'),

    # path('products/<str:ct_models>/<str:slug>/', ProductDetailView.as_view(), name='product_detail'),  # другая модель вывода данных
    # path('', mainapp.product, name='index'),
    path('category/<int:pk>/', product, name='category')
]
