from django.db import models

from products.models import Product


class Order(models.Model):
    customer_name = models.CharField(max_length=100)
    customer_email = models.EmailField()
    customer_address = models.TextField()
    products = models.ManyToManyField(Product, through='OrderItem')
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[
        ('Pending', 'Pending'),
        ('Shipped', 'Shipped'),
        ('Delivered', 'Delivered'),
    ], default='Pending')

    def __str__(self):
        return f'Order {self.id} by {self.customer_name}'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.quantity} of {self.product.name}'
