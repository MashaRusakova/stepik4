from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.decorators import action
from rest_framework.generics import ListCreateAPIView,\
    RetrieveUpdateDestroyAPIView, ListAPIView, RetrieveAPIView,\
    RetrieveUpdateAPIView
from rest_framework.filters import SearchFilter

from .models import ProductSets, Recipient, Order
from .serializer import ProductSetsSerializer,\
    RecipientSerializer, OrderSerializer,\
    RecipientSNPSerializer, OrderChangeAddressSerializer


__all__ = [
    'BeautyboxList',
    'BeautyboxDetail',
    'RecipientList',
    'RecipientDetail',
    'OrderList',
    'OrderDetail',
    'RecipientChangeSNP',
    'OrderChangeAddress',
]


class BeautyboxList(ListAPIView):
    queryset = ProductSets.objects.all()
    serializer_class = ProductSetsSerializer


class BeautyboxDetail(RetrieveAPIView):
    queryset = ProductSets.objects.all()
    serializer_class = ProductSetsSerializer


class RecipientList(ListCreateAPIView):
    queryset = Recipient.objects.all()
    serializer_class = RecipientSerializer


class RecipientDetail(RetrieveUpdateDestroyAPIView):
    queryset = Recipient.objects.all()
    serializer_class = RecipientSerializer


class RecipientChangeSNP(RetrieveUpdateAPIView):
    queryset = Recipient.objects.all()
    serializer_class = RecipientSNPSerializer


class OrderList(ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['delivery_datetime']
    search_fields = ['delivery_datetime']


class OrderDetail(RetrieveUpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderChangeAddress(RetrieveUpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderChangeAddressSerializer

