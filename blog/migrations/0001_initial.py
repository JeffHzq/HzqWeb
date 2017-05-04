# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('modify_time', models.DateTimeField(auto_now=True)),
                ('ico', models.ImageField(null=True, upload_to=b'static/images')),
            ],
        ),
        migrations.CreateModel(
            name='BlogTag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('blog', models.ForeignKey(to='blog.Blog', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='BlogType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=150)),
            ],
        ),
        migrations.AddField(
            model_name='blog',
            name='type',
            field=models.ForeignKey(to='blog.BlogType'),
        ),
    ]
