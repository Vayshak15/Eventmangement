from django.shortcuts import render,redirect
from . models import Event
from .forms import  BookingForm
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def events(request):
    dict_eve={
        'eve': Event.objects.all()
    }
    return render(request,'events.html',dict_eve)
def booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, "Booking confirmed our team will contact you")
            return redirect('/')

    form=BookingForm()
    dict_form={
        'form':form
    }
    return render(request,'booking.html',dict_form)
def contact(request):
    return render(request,'contact.html')
def signin(request):
    return render(request,'signup.html')
def signup(request):
    return render(request,'login.html')