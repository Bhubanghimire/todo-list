from django.shortcuts import render,redirect
from .models import *
from .forms import TodoListForm
from django.views.decorators.http import require_POST


# Create your views here.
def Home(request):
    list_obj = Todolist.objects.all()
    form = TodoListForm()
    param = {"work":list_obj, 'form' : form}
    return render(request,'todolist/index.html',param)


@require_POST
def addTodoItem(request):
    form = TodoListForm(request.POST)

    if form.is_valid():
        new_todo = Todolist(text=request.POST['text'])
        new_todo.save()
    return redirect('index')


def completedTodo(request, todo_id)  :  
    todo = Todolist.objects.get(pk=todo_id)
    todo.completed = True
    todo.save()
    return redirect('index')


def deleteCompleted(request):
    Todolist.objects.filter(completed__exact=True).delete()
    return redirect('index')


def deleteAll(request):
    Todolist.objects.all().delete()
    return redirect('index')