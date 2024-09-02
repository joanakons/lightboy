# Generated by Django 5.1 on 2024-09-01 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_alter_imageupload_image'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ImageUpload',
        ),
        migrations.RemoveField(
            model_name='product',
            name='images',
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/product/'),
        ),
        migrations.AddField(
            model_name='product',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/product/'),
        ),
        migrations.AddField(
            model_name='product',
            name='image3',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/product/'),
        ),
        migrations.AddField(
            model_name='product',
            name='is_sale',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='sale_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
        migrations.AlterField(
            model_name='product',
            name='stock',
            field=models.IntegerField(default=0),
        ),
    ]
