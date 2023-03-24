from django.contrib import admin
# Register your models here.
from .models import Merch, Order

admin.site.register(Order)
admin.site.register(Merch)