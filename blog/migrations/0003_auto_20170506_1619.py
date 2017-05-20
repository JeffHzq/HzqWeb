# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import DjangoUeditor.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20170503_2212'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogtag',
            name='blog',
        ),
        migrations.AddField(
            model_name='blog',
            name='tag',
            field=models.ManyToManyField(to='blog.BlogTag'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='content',
            field=DjangoUeditor.models.UEditorField(default=b'test', verbose_name=b'\xe5\x86\x85\xe5\xae\xb9', blank=True),
        ),
    ]
