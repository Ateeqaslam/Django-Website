from django.http import HttpResponse
from django.shortcuts import redirect, render

from .models import Feedback

# Create your views here.


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def profile(request):
    return render(request, 'profile.html')


def contact_form(request):
    n = request.POST['Name']
    number = request.POST['PhoneNumber']
    mail = request.POST['FromEmailAddress']
    Comment = request.POST['Comments']
    feedback = Feedback(name = n, Pnumber = number,email = mail,comment = Comment)
    feedback.save()
    return redirect(contact)
