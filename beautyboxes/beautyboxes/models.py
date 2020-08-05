from django.db import models
from django.contrib.auth.models import User


class ProductSets(models.Model):   # (набор продуктов)
    title = models.CharField(max_length=500)   # заголовок или наименование
    description = models.TextField(max_length=500, blank=True)   # описание

    def __str__(self):
        return self.title


class Recipient(models.Model):  # получатель
    surname = models.CharField(max_length=20)   # фамилия
    name = models.CharField(max_length=20)    # имя
    patronymic = models.CharField(max_length=20)  # отчество
    phone_number = models.CharField(max_length=15)   # телефон

    def __str__(self):
        return self.surname


class Order(models.Model):    # заказ
    created = 'created'
    delivered = 'delivered'
    processed = 'processed'
    cancelled = 'cancelled'
    Choices = (
        (created, 'created'),
        (delivered, 'delivered'),
        (processed, 'processed'),
        (cancelled, 'cancelled'),
    )
    order_created_datetime = models.DateTimeField()   # дата и время создания заказа
    delivery_datetime = models.DateTimeField()    # дата и время доставки
    delivery_address = models.CharField(max_length=100)    # адрес доставки
    recipient = models.ForeignKey(Recipient,
                           related_name="order",
                           on_delete=models.CASCADE
                           )   # получатель
    product_set = models.ForeignKey(ProductSets,
                             related_name="product_set",
                             on_delete=models.CASCADE
                             )    # набор продуктов
    status = models.CharField(max_length=9, choices=Choices)    # статус

