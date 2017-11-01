# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-10-28 10:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon_code',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coupon_code', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_score', models.IntegerField(default=0)),
                ('review_text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tutor_username', models.CharField(default='NULL', max_length=20)),
                ('stu_username', models.CharField(default='NULL', max_length=20)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('review_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tutorials.Review')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_num', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Tutor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_profile', models.TextField()),
                ('university', models.CharField(max_length=50)),
                ('course_code', models.CharField(max_length=10)),
                ('contacted', models.BooleanField()),
                ('subjects_tags', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('username', models.CharField(default='NULL', max_length=20, primary_key=True, serialize=False)),
                ('password', models.CharField(default='NULL', max_length=20)),
                ('email', models.EmailField(default='NULL', max_length=254)),
                ('phone_num', models.CharField(default='NULL', max_length=15)),
                ('image', models.ImageField(upload_to='photos')),
            ],
        ),
        migrations.CreateModel(
            name='wallet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.FloatField(default=0)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tutorials.User')),
            ],
        ),
        migrations.AddField(
            model_name='tutor',
            name='name',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='tutorials.User'),
        ),
        migrations.AddField(
            model_name='student',
            name='name',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='tutorials.User'),
        ),
        migrations.AddIndex(
            model_name='session',
            index=models.Index(fields=['tutor_username', 'stu_username'], name='tutorials_s_tutor_u_097bb7_idx'),
        ),
    ]