from django.contrib import admin
from blog.models import *
from blog.form import BlogForm

class BlogAdmin(admin.ModelAdmin):
    list_display = ('type', 'title', 'create_time')
    form = BlogForm

admin.site.register(BlogType)
admin.site.register(Blog, BlogAdmin)
admin.site.register(BlogTag)