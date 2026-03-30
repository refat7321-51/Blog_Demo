from django.contrib import admin
from .models import Post, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created_date', 'total_likes']
    list_filter = ['created_date', 'author']
    search_fields = ['title', 'content']
    readonly_fields = ['created_date', 'updated_date']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['author', 'post', 'created_date']
    list_filter = ['created_date', 'author']
    search_fields = ['content']
    readonly_fields = ['created_date']
