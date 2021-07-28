from django.db import models

# Create your models here.
class ProductKeluar(models.Model):
    # category = models.ForeignKey(Category, related_name='cp_out', on_delete=models.DO_NOTHING)
    # product = models.ForeignKey(Product, related_name='product_out', on_delete=models.CASCADE)
    category    = models.CharField(max_length=200, db_index=True)
    product     = models.CharField(max_length=200, db_index=True)
    penerima    = models.CharField(max_length=100)
    total       = models.IntegerField()
    created     = models.DateTimeField(auto_now_add=True)
    updated     = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.category