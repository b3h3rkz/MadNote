# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('madNotes', '0006_descrition'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='note',
            options={'ordering': ['-created'], 'verbose_name': 'Mad Note', 'verbose_name_plural': 'Note Entries'},
        ),
    ]
