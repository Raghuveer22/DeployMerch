from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Order,Merch
from .serializers import MerchSerializer,OrderSerializer

@api_view(['GET'])
def apiOverview(request):
    api_urls={
        'List':'/merch-list/',
        'Detail View':'/merch-detail/<str:pk>/',
        'Create':'/order-add/',
    }
    return Response(api_urls)
@api_view(['GET'])
def merchList(request):
    merchs=Merch.objects.all()
    serializer=MerchSerializer(merchs,many=True)
    return Response(serializer.data)
@api_view(['GET'])
def merchDetail(request,pk):
    merch=Merch.objects.get(id=pk)
    serializer=MerchSerializer(merch)
    return Response(serializer.data)
@api_view(['POST'])
def addOrder(request):
    serializer=OrderSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
@api_view(['GET'])
def orderDetail(request,pk):
    order=Order.objects.get(id=pk)
    serializer=OrderSerializer(order)
    return Response(serializer.data)
