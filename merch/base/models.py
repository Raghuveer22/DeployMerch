# Create your models here.
from django.db import models

# Create your models here.
class Merch(models.Model):
    SIZE_CHOICES = (
        ('S', 'Small 34-37'),
        ('M', 'Medium 38-40'),
        ('L', 'Large 41-43'),
        ('XL', 'XL 44-46'),
        ('XXL', 'XXL 47-50'),
    )
    TYPE_CHOICES = (
        ('T', 'T-Shirts'),
        ('H', 'Hoodie'),
        ('F', 'Featured'),
    )
    photo=models.ImageField(upload_to ='media/')
    name=models.CharField(max_length=100)
    size=models.CharField(max_length=100,choices=SIZE_CHOICES)
    s_type=models.CharField(max_length=100,choices=TYPE_CHOICES)
    cost=models.IntegerField(default=0)
    left=models.IntegerField(default=0)

class Order(models.Model):
    HOSTEL_CHOICES=(
        ('SI', 'SIANG'),
        ('LO', 'LOHIT'),
        ('DH', 'DIHING'),
        ('DI','DISANG'),
        ('SS','SUBHANSRI'),
        ('DS','DHANSRI'),
        ('BH','BHRAHMAPUTRA'),
        ('KM','KAMENG'),
        ('BA','BARAK'),
        ('UM','UMIAM'),
        ('MA','MANAS'),
        ('KA','KAPILI')
    )
    name=models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    room_no=models.IntegerField(default=None)
    hostel=models.CharField(max_length=100,choices=HOSTEL_CHOICES)
    merch=models.ForeignKey(Merch,on_delete=models.CASCADE,default=None)
    quantity=models.IntegerField(default=0)
