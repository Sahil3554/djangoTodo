from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from crudapp.models import Todo
# Create your views here.
def home(request):
    if request.method=="POST":
        name = request.POST.get('name')
        desc = request.POST.get('desc')
        todo = Todo(name=name,desc=desc)
        todo.save()
    todo_list = Todo.objects.all();
    data ={
        "todo_list": todo_list
    }
    return render(request,'index.html',data)
def update(request,id):
    if request.method=="POST":
        name = request.POST.get('name')
        desc = request.POST.get('desc')
        todo = Todo.objects.get(id = id)
        todo.name = name
        todo.desc = desc
        todo.save()
        return redirect('/')
    todo = Todo.objects.get(id=id)
    data ={
        "todo": todo
    }
    return render(request,'update.html',data)
def delete(request,id):
    todo = Todo.objects.get(id=id)
    todo.delete();
    return redirect('/')

