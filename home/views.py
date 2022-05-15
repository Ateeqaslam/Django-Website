from django.http import HttpResponse
from django.shortcuts import redirect, render

from home.models import Feedback

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
    n = request.Post['Name']
    number = request.Post['PhoneNumber']
    mail = request.Post['FromEmailAddress']
    Comment = request.Post['Comments']
    # feedback = Feedback(name = n, Pnumber = number,email = mail,comment = Comment)
    return redirect(contact)
