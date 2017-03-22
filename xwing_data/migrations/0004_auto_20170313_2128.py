# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-13 21:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('xwing_data', '0003_auto_20170313_2046'),
    ]

    operations = [
        migrations.CreateModel(
            name='Upgrade',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=100)),
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('xws', models.CharField(max_length=100)),
                ('is_unique', models.BooleanField(default=False)),
                ('is_limited', models.BooleanField(default=False)),
                ('text', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(upload_to='')),
                ('points', models.IntegerField()),
                ('energy', models.IntegerField(default=0)),
                ('range', models.IntegerField(default=0)),
                ('attack', models.IntegerField(default=0)),
                ('faction', models.ManyToManyField(to='xwing_data.Faction')),
                ('slot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='xwing_data.Slot')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterUniqueTogether(
            name='pilot',
            unique_together=set([('xws', 'faction', 'ship')]),
        ),
    ]
