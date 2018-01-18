from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Todo


def index(request):
    todos = Todo.objects.all()[:10]

    context = {
        'todos': todos
    }
    return render(request, 'index.html', context)


def show(request, id):
    todo = Todo.objects.get(id=id)

    context = {
        'todo': todo
    }
    return render(request, 'show.html', context)


def add(request):
    if(request.method == 'POST'):
        title = request.POST['title']
        text = request.POST['text']

        todo = Todo(title=title, text=text)
        todo.save()

        return redirect('/todos')
    else:
        return render(request, 'add.html')
