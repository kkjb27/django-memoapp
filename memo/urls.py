from django.urls import path
from . import views

app_name = 'memoapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('memo_list/', views.MemoListView.as_view(), name='memo_list'),
    path('memo_detail/<int:id>/', views.MemoDetailView.as_view(), name='memo_detail'),
    path('memo_form/', views.MemoCreateView.as_view(), name='memo_form'),
    path('memo_update/<int:id>/', views.MemoUpdateView.as_view(), name='memo_update'),
    path('memo_delete/<int:id>/', views.MemoDeleteView.as_view(), name='memo_delete'),
]
