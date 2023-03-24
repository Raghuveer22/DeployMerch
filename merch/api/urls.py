from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.apiOverview,name='api-overview'),
    path('merch-list/',views.merchList,name='merch-list'),
    path('merch-detail/<str:pk>',views.merchDetail,name='merch-detail'),
    path('order-add/',views.addOrder,name='add-order'),
    path('order-detail/<str:pk>',views.orderDetail,name='order-detail')
]