# Generated by Django 4.1.6 on 2023-02-03 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='count_items',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='products',
            name='stock',
            field=models.IntegerField(default=0),
        ),
    ]
