from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from cartapp.models import Cart
from mainapp.models import Shoes, Clothes, Toy

# Create your views here.

shoes = Shoes.objects.all()
clothes = Clothes.objects.all()
toys = Toy.objects.all()
products = shoes.union(clothes)


def cart(request):
    content = {}
    return render(request, 'cartapp/cart.html', content)


def cart_add(request, pk):
    product = get_object_or_404(Shoes, pk=pk) # костыль

    basket = Cart.objects.filter(user=request.user, product=product).first()

    if not basket:
        basket = Cart(user=request.user, product=product)

    basket.quantity += 1
    basket.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def cart_remove(request, pk):
    content = {}
    return render(request, 'cartapp/cart.html', content)
