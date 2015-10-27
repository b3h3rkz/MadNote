# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('madNotes', '0004_exuserprofile_is_human'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exuserprofile',
            name='is_human',
            field=models.NullBooleanField(default=None, choices=[('y', 'YES'), ('n', ' NO')]),
        ),
    ]
