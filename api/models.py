from django.db import models

# Create your models here.
class Merekmotor(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Produk(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Merekmotor, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Order(models.Model):
    product = models.ForeignKey(Produk, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    date_ordered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.quantity} - {self.product.name}"