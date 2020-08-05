from django.db import models
from rest_framework.serializers import ModelSerializer

from .models import ProductSets, Recipient, Order


class ProductSetsSerializer(ModelSerializer):
    class Meta:
        model = ProductSets
        fields = [
            'id',
            'title',
            'description',
        ]


class RecipientSerializer(ModelSerializer):
    class Meta:
        model = Recipient
        fields = [
            'id',
            'surname',
            'name',
            'patronymic',
            'phone_number',
        ]


class RecipientSNPSerializer(ModelSerializer):
    class Meta:
        model = Recipient
        fields = [
            'surname',
            'name',
            'patronymic',
        ]


class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = [
            'id',
            'order_created_datetime',
            'delivery_datetime',
            'delivery_address',
            'recipient',
            'product_set',
            'status',
            ]


class OrderChangeAddressSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = [
            'delivery_address',
            ]

