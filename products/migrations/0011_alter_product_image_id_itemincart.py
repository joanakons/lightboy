# Generated by Django 5.1 on 2024-09-03 19:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_rename_birth_date_account_date_of_birth'),
        ('products', '0010_alter_product_image_id_iteminwishlist_wishlist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image_id',
            field=models.CharField(default='af416d7c1565437ab304ad44e92ef4d3', editable=False, max_length=32, unique=True),
        ),
        migrations.CreateModel(
            name='ItemInCart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.product')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='account.account')),
            ],
        ),
    ]
