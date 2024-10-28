# Generated by Django 5.1.2 on 2024-10-28 08:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_name', models.CharField(max_length=100)),
                ('generated', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
                ('season', models.CharField(max_length=100)),
                ('width', models.IntegerField()),
                ('profile', models.CharField(max_length=100)),
                ('diameter', models.CharField(max_length=100)),
                ('speed_index', models.CharField(max_length=100)),
                ('load_index', models.CharField(max_length=100)),
                ('double_load_index', models.CharField(max_length=100)),
                ('photo', models.ImageField(upload_to='products/%Y/%m/%d')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('descriptions', models.TextField()),
                ('number', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.category')),
            ],
        ),
    ]
