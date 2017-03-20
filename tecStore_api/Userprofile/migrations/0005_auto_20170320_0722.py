# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-20 14:22
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Userprofile', '0004_auto_20170319_1500'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=10, null=True)),
                ('location', models.CharField(max_length=50, null=True)),
                ('User', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='item',
            name='first_img',
            field=models.ImageField(default='Images/no-img.png', null=True, upload_to='Images/'),
        ),
        migrations.AlterField(
            model_name='item',
            name='second_img',
            field=models.ImageField(default='Images/no-img.png', null=True, upload_to='Images/'),
        ),
        migrations.AlterField(
            model_name='item',
            name='third_img',
            field=models.ImageField(default='Images/no-img.png', null=True, upload_to='Images/'),
        ),
    ]