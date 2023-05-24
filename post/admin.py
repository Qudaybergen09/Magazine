from django.contrib import admin
from .models import Post,Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    
    list_display = ['id', 'name']
    ordering = ['id']
    search_fields = ['name']

@admin.register(Comment)
class CommentsAdmin(admin.ModelAdmin):
    pass