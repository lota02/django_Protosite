from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(response):
    return render(response,"prototype/home.html",{})

def about(response):
    return render(response,"prototype/about.html",{})

def feedback(response):
    return render(response,"prototype/feedback.html",{})

def contact(response):
    return render(response,"prototype/contact.html",{})


