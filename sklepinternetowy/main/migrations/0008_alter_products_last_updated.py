# Generated by Django 4.1.4 on 2022-12-10 20:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_products_last_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='last_updated',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
