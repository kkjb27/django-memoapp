from django.urls import path
from . import views

app_name = 'memoapp'

urlpatterns = [
    path('', views.index, name='index'),
]
