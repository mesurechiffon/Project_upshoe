# Generated by Django 5.0.2 on 2024-02-21 17:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_shoes', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='my_shoes',
            old_name='perchase_date',
            new_name='purchase_date',
        ),
        migrations.RenameField(
            model_name='my_shoes',
            old_name='perchase_price',
            new_name='purchase_price',
        ),
    ]
