# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-13 15:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='partner_id',
        ),
        migrations.RemoveField(
            model_name='message',
            name='user_id',
        ),
        migrations.AddField(
            model_name='message',
            name='partner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='partner', to='api.DummyUser'),
        ),
        migrations.AddField(
            model_name='message',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user', to='api.DummyUser'),
        ),
    ]