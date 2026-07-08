from django.shortcuts import render, redirect

from .models import mytodolist

from .forms import TodoListForm

from django.views.decorators.http import require_POST

# Create your views here.

def index(request):
    todo_items = mytodolist.objects.order_by('id')
    form = TodoListForm()
    context = {'todo_items' : todo_items, 'form' : form}
    return render(request, 'mytodolist/index.html', context)

@require_POST
def addTodoItem(request):
    form = TodoListForm(request.POST)
    
    if form.is_valid():
        text = form.cleaned_data['text']
        new_todo = mytodolist(text=text)
        new_todo.save()
    
    """ print(request.POST['text']) """
    return redirect('index')


def completedTodo(request, todo_id):
    todo = mytodolist.objects.get(pk=todo_id)
    todo.completed = True
    todo.save()
    
    return redirect('index')


def deleteCompleted(request):
    mytodolist.objects.filter(completed__exact=True).delete()
    
    return redirect('index')


def deleteAllItem(request):
    mytodolist.objects.all().delete()
    
    return redirect('index')