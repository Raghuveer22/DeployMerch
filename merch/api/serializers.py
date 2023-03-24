from rest_framework import serializers
from base.models import Order,Merch

class MerchSerializer(serializers.ModelSerializer):
    class Meta:
        model=Merch
        fields='__all__'
        #required_fields=fields

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model=Order
        fields='__all__'
        #required_fields=fields
        