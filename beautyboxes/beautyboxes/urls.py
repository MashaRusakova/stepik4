from django.contrib import admin
from django.urls import path

from .views import BeautyboxList, BeautyboxDetail,\
    RecipientList, RecipientDetail, OrderList, OrderDetail,\
    RecipientChangeSNP, OrderChangeAddress


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/beautyboxes/', BeautyboxList.as_view(), name='beautybox-List'),
    path('api/beautyboxes/<int:pk>/', BeautyboxDetail.as_view(), name='beautybox-detail'),
    path('api/recipients/', RecipientList.as_view(), name='recipient-List'),
    path('api/recipients/<int:pk>/', RecipientDetail.as_view(), name='recipient-detail'),
    path('api/recipients/<int:pk>/change_snp/', RecipientChangeSNP.as_view(), name='recipientsnd-detail'),
    path('api/orders/', OrderList.as_view(), name='order-List'),
    path('api/orders/<int:pk>/', OrderDetail.as_view(), name='order-detail'),
    path('api/orders/<int:pk>/change_address/', OrderChangeAddress.as_view(), name='change-address'),
]

