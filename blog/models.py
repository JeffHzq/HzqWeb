# -*- coding: utf-8 -*-
from django.db import models
# from DjangoUeditor.models import UEditorField
from pagedown.widgets import AdminPagedownWidget
from django import forms
from tagging.fields import TagField
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

# 文章类型
class BlogType(models.Model):
    name = models.CharField(max_length=150)
    def __str__(self):
        return self.name

# 文章
class Blog(models.Model):
    type = models.ForeignKey(BlogType)
    title = models.CharField(max_length=255)
    content = models.TextField()
    create_time = models.DateTimeField(auto_now_add=True)
    modify_time = models.DateTimeField(auto_now=True)
    ico = models.ImageField(null=True, upload_to="icos/", default="icos/ico_default.jpg")
    tags = TagField(default=[])

    def __str__(self):
        return self.title




