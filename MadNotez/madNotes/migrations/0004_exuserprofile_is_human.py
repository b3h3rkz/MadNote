# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('madNotes', '0003_exuserprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='exuserprofile',
            name='is_human',
            field=models.BooleanField(default=None),
            preserve_default=True,
        ),
    ]
