from django.urls import path
from . import views

app_name= "Europe"

urlpatterns=[
    path('names', views.kindle, name='index'),
]