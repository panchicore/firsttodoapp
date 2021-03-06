from django.template.context import RequestContext
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import get_object_or_404
from tada.models import TodoItem
from tada.models import Todo
from django.shortcuts import render_to_response
from django.http import HttpResponse
# Create your views here.

@staff_member_required
def home(request):
    todos = Todo.objects.all().order_by("id")
    return render_to_response("tada/home.html", {'todos':todos}, context_instance=RequestContext(request))

@staff_member_required
def mark_todo(request):
    todo_item_id = request.GET.get("todo_item_id")
    todo_item = get_object_or_404(TodoItem, id=todo_item_id)
    todo_item.swich()
    
    return HttpResponse(todo_item.hecha)