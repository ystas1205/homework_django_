from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}


def home_page(request):
    return HttpResponse('Главная страница')


def recipes(request, menu):
    serving = int(request.GET.get('serving'))
    dish = DATA.get(menu, None)
    dict_menu = {}
    for recipe, food in dish.items():
        result = {recipe: round(food * serving, 2)}
        dict_menu.update(result)
        print(dict_menu)
    if dish:
        context = {'recipe': dict_menu}
        return render(request, 'calculator/index.html', context)
    else:
        return HttpResponseNotFound("Такого блюда нет в меню")
