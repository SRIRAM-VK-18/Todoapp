from django.shortcuts import render
from .models import mytodolist

# Create your views here.
def index(request):
    todo_items = mytodolist.objects.order_by('id')
    context = {'todo_items' : todo_items}
    return render(request, 'mytodolist/index.html', context)