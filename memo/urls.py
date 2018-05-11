from django.urls import path
from . import views

app_name = 'memoapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('memo_list/', views.MemoListView.as_view(), name='memo_list_view'),
    path('memo_detail/<int:id>/', views.MemoDetailView.as_view(), name='memo_detail_view'),
    path('memo_form/', views.MemoCreateView.as_view(), name='memo_form_view'),
]
