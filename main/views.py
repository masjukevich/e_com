from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    context = {
        'title': 'Мебель здесь',
    }

    return render(
        request,
        'main/index.html',
        context
    )
