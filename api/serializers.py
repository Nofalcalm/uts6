from rest_framework import serializers
from .models import Merekmotor, Produk, Order

class MerekmotorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Merekmotor
        fields = '__all__'

class ProdukSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produk
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'