# Generated by Django 5.1 on 2024-09-07 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0021_alter_product_image_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image_id',
            field=models.CharField(default='e35322ac458141369742bc7fdb5a8443', editable=False, max_length=32, unique=True),
        ),
    ]
