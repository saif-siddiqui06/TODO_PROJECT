# todo/views.py

from django.shortcuts import render , redirect , get_object_or_404 , HttpResponse
from .models import *
from django.shortcuts import render
from .forms import InputForm
from django.urls import reverse, reverse_lazy

def task_list(request):
     if request.method == "POST":
          data = request.POST
          todoTitle = data.get('todoTitle')
          
          Task.objects.create(title=todoTitle,
                              )
          return redirect('.')
     
     tasks = Task.objects.all()
     return render(request, 'task_list.html', {'tasks': tasks})

def delete_task(request, id):
     todo_item = get_object_or_404(Task, pk=id)
     todo_item.delete()
     return redirect('task_list')

def update_task(request, id):
     tasks = Task.objects.get(id=id)
     print(tasks)
     
     if request.method =='POST':
          data = request.POST
          print(data)
          todoTitle = data.get('todoTitle')
          tasks.title = todoTitle
          tasks.save()
          
          return redirect('task_list')

     else :
          return render(request, 'update_todo.html',{'tasks': tasks})     




