# Generated by Django 5.1 on 2024-09-05 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0016_alter_product_image_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image_id',
            field=models.CharField(default='005316669a1c46c9a914c04938517916', editable=False, max_length=32, unique=True),
        ),
    ]
