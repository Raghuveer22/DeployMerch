from django.urls import include,path
from rest_framework import routers
from . import views



urlpatterns = [
    path('api-auth/',include('rest_framework.urls',namespace='rest_framework')),
    path('', views.merch_list, name = 'home'),
    path('merch-detail/<str:size_key>/<str:name>/',views.merch_detail, name = 'merch-detail'),
    path('add-order/<str:pk>', views.add_order, name = 'add-order'),
]