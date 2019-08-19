# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2019-08-18 07:44
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='标签名')),
            ],
            options={
                'verbose_name': '标签',
                'verbose_name_plural': '标签',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='评论内容')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': '题库',
                'verbose_name_plural': '题库',
                'permissions': (('can_change_question', '可以修改题目信息'), ('can_add_question', '可以添加题目信息'), ('can_change_question_status', '可以修改题目状态')),
            },
        ),
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture_url', models.CharField(max_length=100, verbose_name='图片地址')),
                ('status', models.BooleanField(default=False, verbose_name='审核状态')),
                ('pub_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='入库时间')),
                ('category', models.ManyToManyField(null=True, to='picture.Category', verbose_name='所属分类')),
                ('contributor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='贡献者')),
            ],
            options={
                'verbose_name': '图片表',
                'verbose_name_plural': '图片表',
            },
        ),
        migrations.AddField(
            model_name='comment',
            name='photo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='picture.Picture', verbose_name='图片'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='评论人'),
        ),
    ]
