# Generated by Django 5.1 on 2024-09-05 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0015_alter_product_image_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image_id',
            field=models.CharField(default='fdb6ef3860314401a7b6a986b16cdf8e', editable=False, max_length=32, unique=True),
        ),
    ]
