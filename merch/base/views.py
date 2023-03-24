from django.shortcuts import render,redirect
# Create your views here.
from django.shortcuts import render

from .models import Merch,Order

from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.http import Http404
from .forms import AddOrderForm
from django.contrib import messages

from django.core.mail import EmailMessage, get_connection
from django.conf import settings
       
def merch_list(request):
    allMerch = Merch.objects.filter(size='S')
    return  render ( request , 'base/merch_list.html',{'allMerch':allMerch})

def merch_detail(request,size_key,name):
    merch = get_object_or_404(Merch,size=size_key,name=name)
    return  render ( request , 'base/merch_detail.html',{'merch':merch})

def add_order(request,pk):
    merch = get_object_or_404(Merch,id=pk)
    if request.method == 'POST':
        form = AddOrderForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            room_no = form.cleaned_data['room_no']
            hostel = form.cleaned_data['hostel']
            quantity = form.cleaned_data['quantity']
            order = Order(name=name, email=email, room_no=room_no, hostel=hostel,quantity=quantity,merch = merch)
            order.save()
            print(order.id)
            messages.success(request, 'Form submission successful')
            print(form.cleaned_data)
            with get_connection(  
                host=settings.EMAIL_HOST, 
                port=settings.EMAIL_PORT,  
                username=settings.EMAIL_HOST_USER, 
                password=settings.EMAIL_HOST_PASSWORD, 
                use_tls=settings.EMAIL_USE_TLS  
       ) as connection:  
                subject = "Merch"
                email_from = settings.EMAIL_HOST_USER  
                recipient_list = [order.email, ]  
                message = f"order ID{order.id} " 
                html_message = '''<h2>this is {{order.id}} an automated message</h2>'''
                msg = EmailMessage(subject, html_message, email_from,recipient_list, connection=connection)
                attachment="/home/sri-vallabh/Mergeportal/merch/media/media/hoodie.jpg"
                msg.attach_file(attachment)
                msg.content_subtype = "html"
                msg.send()
            return order_detail(request,order.id)
    else:
        form = AddOrderForm()
    return  render ( request , 'base/add_order.html',{'merch':merch,'form':form})

def order_detail(request,pk):
    order = get_object_or_404(Order,id=pk)
    return  render ( request , 'base/order_detail.html',{'order':order})


