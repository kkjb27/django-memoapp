from django.urls import path
from . import views

app_name = 'memoapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('memo_list/', views.list_view, name='list_view'),
]
