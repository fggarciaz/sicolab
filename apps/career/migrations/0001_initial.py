# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-02-15 02:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Career',
            fields=[
                ('id_car', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_car', models.CharField(max_length=100, unique=True)),
                ('section_car', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('id_sem', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_sem', models.CharField(max_length=100)),
                ('parallel_sem', models.CharField(max_length=1)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='career.Career')),
            ],
        ),
    ]
