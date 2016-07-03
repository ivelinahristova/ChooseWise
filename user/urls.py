from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'login/$', views.sign_in, name='sign_in'),
]
