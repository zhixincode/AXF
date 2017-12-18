# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-27 09:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0005_auto_20170927_1537'),
    ]

    operations = [
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productid', models.CharField(max_length=30)),
                ('productimg', models.CharField(max_length=200)),
                ('productname', models.CharField(max_length=200)),
                ('productlongname', models.CharField(max_length=200)),
                ('isxf', models.BooleanField(default=False)),
                ('pmdesc', models.CharField(max_length=30)),
                ('specifics', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('marketprice', models.FloatField()),
                ('categoryid', models.CharField(max_length=20)),
                ('childcid', models.CharField(max_length=200)),
                ('childcidname', models.CharField(max_length=20)),
                ('dealerid', models.CharField(max_length=200)),
                ('storenums', models.IntegerField()),
                ('productnum', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'axf_goods',
            },
        ),
    ]