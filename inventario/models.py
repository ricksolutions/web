from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from productos.models import Product
from proveedores.models import Supplier

class ProductReception(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='receptions')
    supplier = models.ForeignKey(Supplier, on_delete=models.SET_NULL, null=True, related_name='receptions')
    quantity = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.quantity} x {self.product.name} from {self.supplier}"

@receiver(post_save, sender=ProductReception)
def update_stock_on_reception(sender, instance, created, **kwargs):
    if created:
        product = instance.product
        product.stock += instance.quantity
        product.save()
