from .views import *
from django.urls import path,include

urlpatterns = [
    path("",Home,name="index"),
    path('add', addTodoItem, name='add'),
    path('completed/<todo_id>', completedTodo, name='completed'),
    path("deleteall/",deleteAll,name="deleteall"),
    path("deletecompleted/",deleteCompleted,name="completed"),
]
