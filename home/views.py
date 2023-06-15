from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime

from home.models import Contact, Order
from django.contrib import messages


# Create your views here.
def index(request):
    context = {
        'variable1' :'Jazz is great',
        'variable2' :'Danish is great'
    }
    return render(request, 'index.html', context)
    # return HttpResponse('this is homepage')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        desc = request.POST.get('desc')
        contact = Contact(name=name, phone=phone, email=email, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, "Your message has been sent!")


    return render(request, 'contact.html')

def order(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        quantity = request.POST.get('quantity')
        order = Order(name=name, phone=phone, address=address, quantity=quantity, date=datetime.today())
        order.save()
        messages.success(request, "Your message has been sent!")
        
    return render(request, 'order.html')