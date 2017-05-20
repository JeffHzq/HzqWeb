# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import DjangoUeditor.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20170506_1619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='content',
            field=DjangoUeditor.models.UEditorField(verbose_name=b'\xe5\x86\x85\xe5\xae\xb9', blank=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='ico',
            field=models.ImageField(default=b'icos/ico_default.jpg', null=True, upload_to=b'icos/'),
        ),
    ]
