# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-13 19:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BaseSize',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Faction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Pilot',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=100)),
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('xws', models.CharField(max_length=100, unique=True)),
                ('is_unique', models.BooleanField(default=False)),
                ('skill', models.IntegerField()),
                ('points', models.IntegerField()),
                ('ability', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(upload_to='')),
                ('faction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='xwing_data.Faction')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Ship',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=100)),
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('xws', models.CharField(max_length=100, unique=True)),
                ('actions', models.ManyToManyField(to='xwing_data.Action')),
                ('faction', models.ManyToManyField(to='xwing_data.Faction')),
                ('size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='xwing_data.BaseSize')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Slot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=100)),
                ('pilot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='xwing_data.Pilot')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SlotType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Stats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attack', models.IntegerField()),
                ('agility', models.IntegerField()),
                ('hull', models.IntegerField()),
                ('shields', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='slot',
            name='slot_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='xwing_data.SlotType'),
        ),
        migrations.AddField(
            model_name='ship',
            name='stats',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='xwing_data.Stats'),
        ),
        migrations.AddField(
            model_name='pilot',
            name='ship',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='xwing_data.Ship'),
        ),
        migrations.AddField(
            model_name='pilot',
            name='ship_override',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='xwing_data.Stats'),
        ),
    ]
