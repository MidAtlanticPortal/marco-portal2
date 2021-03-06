# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import wagtail.wagtailcore.fields
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20171120_2017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepagecarousel',
            name='body',
            field=wagtail.wagtailcore.fields.RichTextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='homepagecarousel',
            name='slide_image',
            field=models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='base.PortalImage', null=True),
            preserve_default=True,
        ),
    ]
