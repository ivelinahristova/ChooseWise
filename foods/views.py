from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader
from dateutil.parser import parse

from .models import Foods
from .models import Nutrients
from .models import Foods_Nutrients
from .models import ConsumedProducts
from .models import Diet

from .forms import ConsumedProductForm
from .forms import DietForm

def nutrients(request):
    nutrients = Nutrients.objects.all()
    template = loader.get_template('nutrients/list.html')
    context = {
        'nutrients': nutrients,
    }
    return HttpResponse(template.render(context, request))

def index(request):
    nutrients = Nutrients.objects.all()
    template = loader.get_template('foods/index.html')
    context = {
        'nutrients': nutrients
    }
    return HttpResponse(template.render(context, request))

def consumed(request):
    consumed_foods = []
    if request.user.is_authenticated():
        user_id = request.user.id
        consumed_foods = ConsumedProducts.objects.filter(user__id = user_id)
    else:
        user = '11111'

    nutrients = Nutrients.objects.all()
    template = loader.get_template('foods/consumed.html')
    context = {
        'nutrients': nutrients,
        'consumed_foods': consumed_foods
    }
    return HttpResponse(template.render(context, request))

def add(request):
    consumed_food = ''
    form = ConsumedProductForm()
    if request.method == 'POST':
        food_id = int(request.POST['foods'])
        date = parse(request.POST['date'])
        count = int(request.POST['count'])
        food = Foods.objects.get(food_id = food_id)
        consumed_food = ConsumedProducts(date = date, count = count, food = food, user = request.user)
        consumed_food.save()

    template = loader.get_template('foods/add.html')
    context = {
        'consumed_food': consumed_food,
        'form': form
    }
    return HttpResponse(template.render(context, request))

def list(request):
    foods = Foods.objects.all()

    template = loader.get_template('foods/list.html')
    context = {
        'foods': foods,
    }
    return HttpResponse(template.render(context, request))

def suggest(request):

    user_id = request.user.id
    diet_elements = Diet.objects.filter(user__id = user_id)
    consumed_nutrients = dict()    
   
    consumed_foods = ConsumedProducts.objects.filter(user__id = user_id)
    for consumed_food in consumed_foods:
        nutrients = Foods_Nutrients.objects.filter(food__food_id = consumed_food.id)
        # return HttpResponse(diet_element.nutrient.nutrient_id)
        for nutrient in nutrients:
            if nutrient.nutrient_id in consumed_nutrients.keys():
                consumed_nutrients[nutrient.nutrient_id] += nutrient.grams * consumed_food.count
            else:
                consumed_nutrients[nutrient.nutrient_id] = nutrient.grams * consumed_food.count

    nutrients = dict()
    for diet_element in diet_elements:
        if consumed_nutrients[diet_element.nutrient.nutrient_id] < diet_element.grams:
            nutrients[diet_element.nutrient.nutrient_id] = diet_element.grams - consumed_nutrients[diet_element.nutrient.nutrient_id]

    foods = []
    for nutrient_id, grams in nutrients.items():
        foods.extend(Foods_Nutrients.objects.filter(nutrient__nutrient_id=nutrient_id, grams__lte = grams).select_related())

    template = loader.get_template('foods/suggest.html')
    context = {
        'foods': foods,
    }
    return HttpResponse(template.render(context, request))


def diet_add(request):
    user_id = request.user.id
    diets = Diet.objects.filter(user__id = user_id)
    form = DietForm()
    if request.method == 'POST':
        nutrient_id = int(request.POST.get('nutrient', False))
        grams = int(request.POST.get('grams', False))
        nutrient = Nutrients.objects.get(nutrient_id = nutrient_id)
        diet = Diet(grams = grams, nutrient = nutrient, user = request.user)
        diet.save()

    template = loader.get_template('diet/add.html')
    context = {
        'diets': diets,
        'form': form
    }

    return HttpResponse(template.render(context, request))

def diet_delete(request, diet_id):
    diet = Diet.objects.get(id = diet_id)
    diet.delete()

    return HttpResponseRedirect('/foods/diet/')
