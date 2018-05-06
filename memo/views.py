from django.shortcuts import render
from memo.models import Memo


def index(request):
    return render(request, 'memo/index.html', {'text': 'Hello World!'})


def list_view(request):
    return render(request, 'memo/memo_list.html', {'memos': Memo.objects.all()})
