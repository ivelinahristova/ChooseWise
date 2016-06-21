from django.contrib import admin

# Register your models here.
from .models import Nutrient_Categories
from .models import Nutrients
from .models import Foods
from .models import Foods_Nutrients

admin.site.register(Nutrient_Categories)
admin.site.register(Nutrients)
admin.site.register(Foods)
admin.site.register(Foods_Nutrients)