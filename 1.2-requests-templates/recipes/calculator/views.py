from django.shortcuts import render

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

def home_view(request):
    return HttpResponse('Привет, это помощник для приготовления блюд!')

def calculator(request, recipe):
    servings = int(request.GET.get('servings', 1))
    context = {'recipe':{}}
    for ingredient, amount in DATA[recipe].items():
        context['recipe'][ingredient] = round((amount * servings), 2)
    return render(request, 'calculator/index.html', context)
