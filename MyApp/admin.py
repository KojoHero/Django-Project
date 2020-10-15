from django.contrib import admin
from .models import CreateUserForm, Post
from . import models

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

class TodoListAdmin(admin.ModelAdmin):
    list_display = ("title",  "created", "due_date")


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)


admin.site.register(models.TodoList, TodoListAdmin)
admin.site.register(models.Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(CreateUserForm)
# admin.site.register(Project)



