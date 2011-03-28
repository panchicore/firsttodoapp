from tada.models import Todo
from tada.models import TodoItem
from django.contrib import admin

class TodoItemInline(admin.TabularInline):
    model = TodoItem
    extra = 1

class TodoAdmin(admin.ModelAdmin):
    inlines = [TodoItemInline]


admin.site.register(Todo, TodoAdmin)
