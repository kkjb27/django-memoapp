from django.shortcuts import render
from django.views.generic import ListView, DetailView
from memo.models import Memo


def index(request):
    """Index page"""
    return render(request, 'memo/index.html', {'text': 'Hello World!'})


class MemoListView(ListView):
    """メモ一覧ページ"""
    model = Memo  # モデルを指定
    # queryset = Memo.objects.all() # これも一緒
    template_name = 'memo/memo_list.html'  # 表示するHTMLを指定. デフォルトは<app_name>/<model_name>_list.html
    context_object_name = 'memo_list'  # HTMLに渡す変数の名前を指定. デフォルトは<model_name>_listかobject_list


class MemoDetailView(DetailView):
    """メモ詳細ページ"""
    model = Memo
    template_name = 'memo/memo_detail.html'  # 省略可
    context_object_name = 'memo'  # 省略可
    pk_url_kwarg = 'id'  # 指定しないとpk
