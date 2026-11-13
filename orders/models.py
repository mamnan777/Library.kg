from django.db import models


class Order(models.Model):
    STATUS_CHOICES = [
        ('new', 'Новый'),
        ('assembling', 'Сборка'),
        ('shipped', 'В пути'),
        ('delivered', 'Доставлен'),
        ('cancelled', 'Отменён'),
    ]

    order_number = models.CharField(max_length=20, unique=True)
    product_name = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
    customer_name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')
    created_at = models.DateTimeField(auto_now_add=True)

    def total(self):
        return self.price * self.quantity

    def str(self):
        return f'№{self.order_number} {self.product_name}'