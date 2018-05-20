from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Memo
from .forms import MemoForm
from django.urls import reverse_lazy


class MemoListView(ListView):
    """メモ一覧ページ"""
    model = Memo  # モデルを指定
    template_name = 'memo/memo_list.html'  # 表示するHTMLを指定. デフォルトは<app_name>/<model_name>_list.html
    context_object_name = 'memo_list'  # HTMLに渡す変数の名前を指定. デフォルトは<model_name>_listかobject_list


class MemoDetailView(DetailView):
    """メモ詳細ページ"""
    model = Memo
    template_name = 'memo/memo_detail.html'  # 省略可
    context_object_name = 'memo'  # 省略可
    pk_url_kwarg = 'id'  # 指定しないとpk


class MemoCreateView(CreateView):
    """メモ作成ページ"""
    model = Memo
    form_class = MemoForm
    template_name = 'memo/memo_form.html'  # 省略可
    success_url = reverse_lazy('memoapp:memo_list')


class MemoUpdateView(UpdateView):
    """メモ編集ページ"""
    model = Memo
    form_class = MemoForm
    template_name = 'memo/memo_update_form.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('memoapp:memo_list')


class MemoDeleteView(DeleteView):
    """メモ削除ページ"""
    model = Memo
    template_name = 'memo/memo_confirm_delete.html'  # 省略可
    pk_url_kwarg = 'id'  # 指定しないとpk
    success_url = reverse_lazy('memoapp:memo_list')  # 成功したら一覧ページに飛ぶ
