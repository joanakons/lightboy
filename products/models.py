import os
import uuid
from django import forms
from django.db import models
from django.utils.deconstruct import deconstructible


class Category(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'products_category'  # Specify the exact table name in the database

    def __str__(self):
        return self.name

    def get_subcategories(self):
        return Subcategory.objects.filter(parent=self)

    def get_subcategories_dict(self):
        subcategories = Subcategory.objects.filter(parent=self)
        return {
            self.name: list(subcategories.values('name', 'description'))
        }


class Subcategory(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(blank=True, null=True)
    parent = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='children', blank=True, null=True)

    def __str__(self):
        return self.name


@deconstructible
class PathAndRename:
    def __init__(self, path):
        self.path = path

    def __call__(self, instance, filename):
        ext = filename.split('.')[-1]
        sequence = '00'

        # Determine the sequence number based on the field name
        if hasattr(instance, 'image') and filename == instance.image.name:
            sequence = '01'
        elif hasattr(instance, 'image2') and filename == instance.image2.name:
            sequence = '02'
        elif hasattr(instance, 'image3') and filename == instance.image3.name:
            sequence = '03'

        # Generate the filename using the unique_id
        filename = f'{instance.image_id}-{sequence}.{ext}'
        return os.path.join(self.path, filename)


# Instantiate the class with your desired path
upload_to = PathAndRename('product/')


class Product(models.Model):
    name = models.CharField(max_length=30)
    brand = models.CharField(max_length=30, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', blank=True, null=True)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE, blank=True, null=True)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=6)
    stock = models.IntegerField(default=0)
    image_id = models.CharField(max_length=32, unique=True, editable=False, default=uuid.uuid4().hex)
    # image_id = models.CharField(max_length=32,  blank=True, null=True, default=uuid.uuid4().hex)
    image = models.ImageField(upload_to=upload_to, blank=True, null=True)
    image2 = models.ImageField(upload_to=upload_to, blank=True, null=True)
    image3 = models.ImageField(upload_to=upload_to, blank=True, null=True)
    is_sale = models.BooleanField(default=False)
    sale_price = models.DecimalField(default=0, decimal_places=2, max_digits=6)
    added_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # lumens=
    # colour=
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # Generate a unique_id if it doesn't exist
        if not self.image_id:
            self.image_id = uuid.uuid4().hex  # Generate a 32-character unique ID

        # Save the instance with the unique_id
        super(Product, self).save(*args, **kwargs)


# afiseaza pretul cosului abia cand dai comanda
# cosul - alta aplicatie si model, view etc. cu verificare daca mai este in stoc
# adaugarea - functie nu clasa (cart item), buton de dat comanda, stocare preturi produse


# Intrebari:
# chestia cu objects.filter.all
# toate fields in add product form

