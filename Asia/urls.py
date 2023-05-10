from django.urls import path
from . import views

app_name="Asia"

urlpatterns=[
    path('names', views.home, name='index'),
]