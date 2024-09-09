from django.db import models

from account.models import Account
from products.models import Product


#
# class Order(models.Model):
#     customer_name = models.CharField(max_length=100)
#     customer_email = models.EmailField()
#     customer_address = models.TextField()
#     products = models.ManyToManyField(Product, through='OrderItem')
#     order_date = models.DateTimeField(auto_now_add=True)
#     status = models.CharField(max_length=20, choices=[
#         ('Pending', 'Pending'),
#         ('Shipped', 'Shipped'),
#         ('Delivered', 'Delivered'),
#     ], default='Pending')
#
#     def __str__(self):
#         return f'Order {self.id} by {self.customer_name}'


class Order(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='Processing')

    def __str__(self):
        return f"Order {self.id} by {self.user.username}"

    def get_total(self):
        return sum(item.get_total_item_price() for item in self.items.all())


# apasare buton comanda
# 1. create obiect din clasa: class Order (User_if fk, created_at, active)#
# 2. creare obiecte din clasa: class OrderItem(order_id fk, product_name, product.price, quantity,  )
# pentru fiecare obiect IteminCart al userului logat
# pentru fiecare obiect de tip OrderItem creat, se va actualiza stocul produsului respectiv si in acelasi timp dezactivam fiecare ItemInCart
# 4. trimitere mail catre utilizator cu comanda si informatiile aferente


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.product.name}"

    def get_total_item_price(self):
        return self.quantity * self.product.price

# class OrderDetail(models.Model):
#     user = models.ForeignKey(Account, on_delete=models.CASCADE)
#
#     # other fields...
#
#     @classmethod
#     def get_user_orders(cls, user):
#         """Class method to get the first order or all orders for a user."""
#         return cls.objects.filter(user=user)
#
#     @classmethod
#     def get_latest_order(cls, user):
#         """Class method to get the latest order for a user."""
#         return cls.objects.filter(user=user).first()
