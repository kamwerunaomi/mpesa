# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-28 15:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('date_of_transaction', models.DateTimeField()),
                ('transaction_type', models.CharField(max_length=20)),
                ('cost', models.IntegerField()),
                ('phonenumber', models.CharField(max_length=10)),
            ],
        ),
    ]
