# Generated by Django 2.2 on 2023-01-21 07:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_products'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='available',
        ),
    ]
