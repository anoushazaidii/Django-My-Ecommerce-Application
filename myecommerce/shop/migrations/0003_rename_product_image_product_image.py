# Generated by Django 5.0.6 on 2024-05-29 10:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_product_product_category_product_product_image_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='product_image',
            new_name='image',
        ),
    ]
