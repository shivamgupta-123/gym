from django.shortcuts import render, HttpResponse, redirect
import smtplib
from django.contrib.auth import authenticate, login, logout
from .models import Detail
from .models import Contact
from .models import Book
from .models import Comments
from django.contrib.auth.models import User
from django.contrib import messages
import json
from tkinter import ttk
from tkinter import Tk
from django.views.generic import TemplateView, ListView, View
from django.views.generic.edit import FormView
import time
from .forms import *
import os
import requests
from django.core.serializers import serialize
def index(request):
    print(time.strftime('%H:%M:%S'))
    name = request.POST.get('name', 'default')
    phone = request.POST.get('phone', 'default')
    message = request.POST.get('message', 'default')
    information = Detail(name=name, phone=phone, message=message)
    if Detail.objects.filter(name__exact=name):
        return render(request, 'error.html')
    elif name != 'default':
        information.save()

    with open("record.txt", "w+") as f:
        print(f.write(f"{name, phone, message}\n"))
    f.close()
    return render(request, 'index.html')

def signup(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        users = request.POST['username']
        email = request.POST['email']
        if request.POST['password'] == request.POST['confirm_password'] and len(request.POST['password']) > 8:
            try:
                user = User.objects.get(username=users)
                return render(request, 'signup.html', {'error': 'Username already exist, Please Try Again'})
            except User.DoesNotExist:
                user = User.objects.create_user(username=users, password=request.POST['password'])
                user.first_name = first_name
                user.last_name = last_name
                user.email = email
                user.save()
                messages.success(request, "Your Account created Successfully")
                return redirect('/index')
        else:
            return render(request, 'signup.html', {'errors': 'Password not Match and your password length should be 8 character , Please Try Again'})
    return render(request, 'signup.html')

def Login(request):
    if request.method == 'POST':
        uname = request.POST['uname']
        psw = request.POST['psw']
        user = authenticate(username=uname, password=psw)
        clientkey = request.POST['g-recaptcha-response']
        secretkey = '6LdQWfYUAAAAAK8Zl7qVm4weoHd7SuKkVB_hl96V'
        Captcha = {
            'secret': secretkey,
            'response': clientkey
        }
        r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=Captcha)
        response = json.loads(r.text)
        verify = response['success']
        print('Your success is :', verify)
        if user is not None:
            login(request, user)
            detail = Detail.objects.filter(name=uname)
            return render(request, 'see.html', {'users': detail})
        else:
            return render(request, 'login.html', {'error': "Do not match login detail"})
    else:
        return render(request, 'login.html')

def about(request):
    return render(request, 'about.html')

def schedule(request):
    return render(request, 'schedule.html')

def gallery(request):
    return render(request, 'gallery.html')

def blog(request):
    return render(request, 'blog.html')

def blog1(request):
    return render(request, 'blog1.html')

def contact(request):
    a = request.POST.get('a', 'default')
    b = request.POST.get('b', 'default')
    c = request.POST.get('c', 'default')
    info = Contact(a=a, b=b, c=c)
    if Contact.objects.filter(a__exact=a):
        return render(request, 'error.html')
    elif a != 'default':
        info.save()
        connect = smtplib.SMTP("smtp.gmail.com", 587)
        connect.ehlo()
        connect.starttls()
        connect.login("sg242958@gmail.com", "raanheshma")
        mail = "Congratulation\nHi Dear" + a + "\nYou are successful registered in Gym Course"
        connect.sendmail('sg242958@gmail.com', b, mail)
        connect.close()
    return render(request, 'contact.html')

def book(request):
    names = request.POST.get('names', 'default')
    emails = request.POST.get('emails', 'default')
    phones = request.POST.get('phones', '8057527360')
    addresses = request.POST.get('addresses', 'default')
    fnames = request.POST.get('fnames', 'default')
    mnames = request.POST.get('mnames', 'default')
    category = request.POST.get('category', 'General')
    fees = request.POST.get('fees', '1800')
    det = Book(names=names, emails=emails, phones=phones, addresses=addresses, fnames=fnames, mnames=mnames, category=category, fees=fees)
    if Book.objects.filter(emails__exact=emails):
        return render(request, 'error.html')
    elif emails != 'default' and names.count(Book.objects.filter(names__exact=names)) <= 100:
        fees = fees-fees*0.5
        fees = request.POST.get('fees', '1800')
        det.save()
        connect = smtplib.SMTP("smtp.gmail.com", 587)
        connect.ehlo()
        connect.starttls()
        connect.login("sg242958@gmail.com", "raanheshma")
        mailer = "Congratulation\nHi Dear " + names + "\nYour seat booked for this Course"
        connect.sendmail('sg242958@gmail.com', emails, mailer)
        connect.close()
    return render(request, 'book.html')

def comments(request):
    if request.method == 'POST':
        comment = request.POST['comment']
        user = request.user
        parentcomment = request.POST['parentcomment']
        if comment == '':
            return render(request, 'comments.html', {'error': "Please Enter Your Comment"})
        else:
            com = Comments.objects.create(user=user, comment=comment)
            com.save()
            messages.success(request, 'Your Comment post successfully')
            return redirect('/comments')
    commentes = Comments.objects.all()

    return render(request, 'comments.html', {'stu': commentes})

def search(request):
    se = request.GET.get('sea', False)
    s = Detail.objects.filter(name__contains=se)
    return render(request, 'search.html', {'s': s})
