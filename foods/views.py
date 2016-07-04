from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from dateutil.parser import parse

from .models import Foods
from .models import Nutrients
from .models import Foods_Nutrients
from .models import ConsumedProducts

from .forms import ConsumedProductForm

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
        food_id = 1
        date = parse("2015-02-24T13:00:00-08:00")
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

