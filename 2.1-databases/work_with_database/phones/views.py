from django.shortcuts import render, redirect, reverse
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    phone_objects = Phone.objects.all()
    context = {'phones': phone_objects}
    sort = request.GET.get('sort')
    if sort == 'name':
        sort_phone_name = Phone.objects.order_by('name')
        context = {'phones': sort_phone_name}
        return render(request, template, context)
    if sort == 'min_price':
        sort_phone_min = Phone.objects.order_by('price')
        context = {'phones': sort_phone_min}
        return render(request, template, context)
    if sort == 'max_price':
        sort_phone_max = Phone.objects.order_by('-price')
        context = {'phones': sort_phone_max}
        return render(request, template, context)
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone_name = Phone.objects.get(slug=slug)
    context = {'phone': phone_name}
    return render(request, template, context)
