# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-02-15 02:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('distributive', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id_stu', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dni_stu', models.CharField(max_length=10, unique=True)),
                ('password_stu', models.CharField(max_length=200)),
                ('names_stu', models.CharField(max_length=150)),
                ('email_stu', models.EmailField(max_length=100, unique=True)),
                ('token_reset', models.CharField(max_length=200)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('status_stu', models.SmallIntegerField()),
                ('dist', models.ManyToManyField(blank=True, to='distributive.Distributive')),
            ],
        ),
    ]
