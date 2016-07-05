from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib.auth import authenticate, login, logout

from foods.models import ConsumedProducts
from foods.models import Diet
from foods.models import Foods_Nutrients

def sign_in(request):

    username = request.POST.get('username', False)
    password = request.POST.get('password', False)
    
    user = authenticate(username=username, password=password)
    message = None
    if user is not None:
        if user.is_active:
            login(request, user)
            message = 'success'
            # Redirect to a success page.
        else:
            # Return a 'disabled account' error message
            message = 'disabled account'

    else:
        # Return an 'invalid login' error message.
        message = 'invalid login'

    template = loader.get_template('user/login.html')
    context = {
        'message': message,
    }
    return HttpResponse(template.render(context, request))

def sign_out(request):
    logout(request)
    return HttpResponseRedirect('/foods/')

def profile(request):
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
        nutrients[diet_element.nutrient.name] = [
        consumed_nutrients[diet_element.nutrient.nutrient_id] * 100 / diet_element.grams,
        consumed_nutrients[diet_element.nutrient.nutrient_id],
        diet_element.grams
        ]

    template = loader.get_template('user/profile.html')
    context = {
        'nutrients': nutrients,
    }
    return HttpResponse(template.render(context, request))
