from django.shortcuts import render, HttpResponse
from datetime import datetime
from store.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,'index.html')
    #return HttpResponse("this is home page")

def products(request):
    #return HttpResponse("this is products page")
    return render(request,'products.html')

def services(request):
    return render(request,'services.html')
    #return HttpResponse("this is services page")

def ship(request):
    return render(request,'ship.html')
    #return HttpResponse("this is ship page")

def happy(request):
    return render(request,'happy.html')
    #return HttpResponse("this is happy page")

def care(request):
    return render(request,'care.html')
    #return HttpResponse("this is care page")

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date = datetime.today())
        contact.save()
        
    return render(request, 'contact.html')
 