# Generated by Django 2.0.3 on 2018-06-17 16:41

import django.contrib.postgres.fields
import django.contrib.postgres.fields.jsonb
import django.contrib.postgres.fields.ranges
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessEntity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.CharField(editable=False, max_length=50)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('modified_by', models.CharField(editable=False, max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Calendar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.CharField(editable=False, max_length=50)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('modified_by', models.CharField(editable=False, max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.CharField(editable=False, max_length=50)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('modified_by', models.CharField(editable=False, max_length=50)),
                ('name', models.CharField(max_length=10, unique=True)),
                ('full_name', models.CharField(max_length=50)),
                ('display_format', models.CharField(max_length=50)),
                ('flag', models.CharField(max_length=10)),
            ],
            options={
                'verbose_name_plural': 'currencies',
            },
        ),
        migrations.CreateModel(
            name='CurrencyPair',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.CharField(editable=False, max_length=50)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('modified_by', models.CharField(editable=False, max_length=50)),
                ('name', models.CharField(max_length=10, unique=True)),
                ('display_format', models.CharField(max_length=50)),
                ('base_ccy', models.CharField(max_length=10)),
                ('alt_ccy', models.CharField(max_length=10)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Exchange',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.CharField(editable=False, max_length=50)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('modified_by', models.CharField(editable=False, max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='HelloWorldEntity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.CharField(editable=False, max_length=50)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('modified_by', models.CharField(editable=False, max_length=50)),
                ('name', models.CharField(max_length=10, unique=True)),
                ('array_field', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=10), size=8)),
                ('json_field', django.contrib.postgres.fields.jsonb.JSONField()),
                ('integer_range_field', django.contrib.postgres.fields.ranges.IntegerRangeField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Instrument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.CharField(editable=False, max_length=50)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('modified_by', models.CharField(editable=False, max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='InterestRate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.CharField(editable=False, max_length=50)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('modified_by', models.CharField(editable=False, max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Security',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.CharField(editable=False, max_length=50)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('modified_by', models.CharField(editable=False, max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
