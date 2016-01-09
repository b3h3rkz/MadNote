# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('madNotes', '0002_note_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tags',
            name='label',
        ),
        migrations.AddField(
            model_name='tags',
            name='slug',
            field=models.SlugField(default='', unique=True, max_length=30),
            preserve_default=True,
        ),
    ]
