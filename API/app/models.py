from django.db import models

# Create your models here.

class Trufas(models.Model):
    id_trufa = models.IntegerField(primary_key=True,editable=False)
    productName = models.CharField(max_length=255)
    price = models.FloatField()
    image = models.CharField(max_length=1000)

#   productName: 'trufa-limao',
#     price:2.50,
#     productImage: limao
#   }