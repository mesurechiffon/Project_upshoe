# Generated by Django 5.0.2 on 2024-02-21 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='My_shoes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=100)),
                ('model_name', models.CharField(max_length=100)),
                ('model_num', models.CharField(max_length=50)),
                ('release_date', models.DateField()),
                ('release_price', models.IntegerField()),
                ('perchase_date', models.DateField()),
                ('perchase_price', models.IntegerField()),
            ],
        ),
    ]
