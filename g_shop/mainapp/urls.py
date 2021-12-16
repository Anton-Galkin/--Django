from django.urls import path


from .views import ProductDetailView
# from mainapp.views import mainapp
import mainapp.views as mainapp


app_name = 'mainapp'


urlpatterns = [
    path('products/<str:ct_models>/<str:slug>/', ProductDetailView.as_view(), name='product_detail'),  # другая модель вывода данных
    path('', mainapp.product, name='index'),
    path('<int:pk>/', mainapp.product, name='category')
]
