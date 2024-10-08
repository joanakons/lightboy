# Generated by Django 5.1 on 2024-09-04 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_alter_product_image_id_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemincart',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='image_id',
            field=models.CharField(default='17c99d1683eb40ae96d357f93c6e35fb', editable=False, max_length=32, unique=True),
        ),
        migrations.DeleteModel(
            name='Wishlist',
        ),
    ]
