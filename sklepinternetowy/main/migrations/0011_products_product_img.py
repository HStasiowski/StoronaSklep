# Generated by Django 4.1.6 on 2023-02-03 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_cart_count_items_alter_products_stock'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='product_img',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]
