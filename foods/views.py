from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Nutrients

def index(request):
    nutrients = Nutrients.objects.all()
    template = loader.get_template('nutrients/list.html')
    context = {
        'nutrients': nutrients,
    }
    return HttpResponse(template.render(context, request))


