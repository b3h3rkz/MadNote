# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('madNotes', '0005_auto_20151027_0053'),
    ]

    operations = [
        migrations.CreateModel(
            name='Descrition',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.SlugField(max_length=30)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
