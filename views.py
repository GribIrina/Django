from django.shortcuts import render, redirect
from .models import Cardio
from .forms import CardioForm


def index(request):
    tasks = Cardio.objects.order_by('id')
    return render(request, 'main/index.html', {'title': 'Главная страница сайта', 'tasks': tasks})


def about(request):
    return render(request, 'main/about.html')


def create(request):
    error = ''
    if request.method == 'POST':
        form = CardioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма заполнена неверно'
    form = CardioForm(request.POST or None)
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', context)
