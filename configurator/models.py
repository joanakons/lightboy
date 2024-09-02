from django.db import models


class Configurator(models.Model):
    room = models.CharField(max_length=15)
    area = models.IntegerField()
    number_of_outlets = models.IntegerField()
    # name = models.CharField(max_length=30)
    # brand = models.CharField(max_length=30, blank=True, null=True)
    # category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', blank=True, null=True)
    # subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE, blank=True, null=True)
    # price = models.DecimalField(max_digits=10, decimal_places=2)
    # stock = models.IntegerField()
    # images = models.ImageField(upload_to='product_images/')
    # added_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.room
