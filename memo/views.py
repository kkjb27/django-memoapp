from django.shortcuts import render

def index(request):
    return render(request, 'memo/index.html', {'text': 'Hello World!'})
