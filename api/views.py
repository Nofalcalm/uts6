from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Merekmotor, Produk, Order
from .serializers import MerekmotorSerializer, ProdukSerializer, OrderSerializer

class MerekmotorViewSet(viewsets.ModelViewSet):
    queryset = Merekmotor.objects.all()
    serializer_class = MerekmotorSerializer

class ProdukViewSet(viewsets.ModelViewSet):
    queryset = Produk.objects.all()
    serializer_class = ProdukSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer