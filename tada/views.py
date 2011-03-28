from django.template.context import RequestContext
from django.contrib.admin.views.decorators import staff_member_required
from tada.models import TodoItem
from tada.models import Todo
from django.shortcuts import render_to_response
from django.http import HttpResponse
# Create your views here.

def home(request):
    todos = Todo.objects.all().order_by("id")
    return render_to_response("tada/home.html", {'todos':todos}, context_instance=RequestContext(request))

def mark_todo(request):
    todo_item_id = request.GET.get("todo_item_id")
    todo_item = TodoItem.objects.get(id=todo_item_id)

    if todo_item.hecha:
        todo_item.hecha = False
    else:
        todo_item.hecha = True

    todo_item.save()
    
    return HttpResponse(unicode(todo_item.hecha))