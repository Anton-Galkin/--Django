from django.shortcuts import render


# Create your views here.

def main(request):
    return render(request, 'mainapp/index.html')


def product(request):
    return render(request, 'mainapp/products.html')


def contact(request):
    return render(request, 'mainapp/contact.html')


def about(request):
    return render(request, 'mainapp/about.html')
