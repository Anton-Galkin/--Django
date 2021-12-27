"""g_shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from mainapp.views import main, product, contact, about

# from mainapp.views import ProductDetailView


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('admin/', include('adminapp.urls', namespace='admin')),

    path('', include('mainapp.urls', namespace='main')),  #

    # path('', main, name='index'),
    # path('products/', product, name='products'),
    # path('products/', include('mainapp.urls', namespace='products')),
    # path('contact/', contact, name='contact'),
    # path('about/', about, name='about'),

    # path('products_all', product, name='products_all'),
    # path('products_recommendation', product, name='products_recommendation'),
    # path('products_action', product, name='products_action'),
    # path('products_sale', product, name='products_sale'),

    path('auth/', include('authapp.urls', namespace='auth')),
    path('cart/', include('cartapp.urls', namespace='cart')),

    # path('products/<str:ct_models>/<str:slug>/', ProductDetailView.as_view(), name='product_detail')  # Для отображения по другому
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
