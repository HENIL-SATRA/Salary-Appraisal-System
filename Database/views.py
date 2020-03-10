from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django import forms
from .models import userInfo
from .models import userProfile
from .forms import suform
from django.db import models


# Create your views here.
def signup(request):
    return render(request, "signup.html")


def signupform(request):
    if request.method == 'POST':
        ui = userInfo()
        a = request.POST.get('desig', False)
        print(a)
        ui.first = request.POST.get('first')
        ui.last = request.POST.get('last')
        snum = request.POST.get('number')
        print(snum)
        snu = int(snum)
        ui.ssn = snum
        ui.designation = a
        ui.pw = request.POST.get('password')
        ui.save()

        return HttpResponseRedirect(reverse('profile', args=(snu,)))
    else:
        return render(request, "signup.html")


def welcome(request):
    return render(request, "welcome.html")


def selectType(request):
    return render(request, "selectType.html")


def signinit(request):
    if request.method == "POST":
        up = userProfile()
        ss = request.POST.get('ssn')
        ui = userProfile.objects.get(ssn__exact=ss)
        pw = request.POST.get('pwd')
        if userInfo.objects.get(ssn__exact=ss):
            info = userInfo.objects.get(ssn__exact=ss)
            if pw == info.pw and ui.job == "IT":
                return HttpResponseRedirect(reverse('it'))
            else:
                return render(request, "signinit.html")

        return render(request, "signinit.html")
    else:
        return render(request, "signinit.html")


def signinhr(request):
    if request.method == "POST":
        up = userProfile()
        ss = request.POST.get('ssn')
        ui = userProfile.objects.get(ssn__exact=ss)
        pw = request.POST.get('pwd')
        if userInfo.objects.get(ssn__exact=ss):
            info = userInfo.objects.get(ssn__exact=ss)
            if pw == info.pw and ui.job == "HR":
                return HttpResponseRedirect(reverse('hr'))
            else:
                return render(request, "signinhr.html")

        return render(request, "signinhr.html")
    else:
        return render(request, "signinhr.html")


def signinemp(request):
    if request.method == "POST":
        up = userProfile()
        ss = request.POST.get('ssn')
        ui = userProfile.objects.get(ssn__exact=ss)
        pw = request.POST.get('pwd')

        if userInfo.objects.get(ssn__exact=ss):
            info = userInfo.objects.get(ssn__exact=ss)
            if pw == info.pw and ui.job == "EMP":
                return HttpResponseRedirect(reverse('emp'))
            else:
                return render(request, "signinemp.html")

        return render(request, "signinemp.html")
    else:
        return render(request, "signinemp.html")


def profile(request, sn):
    context = {'foo': sn}

    return render(request, "profile.html", context)


def profileform(request):
    if request.method == "POST":
        up = userProfile()
        up.dob = request.POST.get('dob')
        up.ssn = request.POST.get('num')
        up.gender = request.POST.get('gender', False)
        up.doj = request.POST.get('doj')
        up.city = request.POST.get('cs', False)
        up.job = request.POST.get('job', False)
        up.save()
        return HttpResponseRedirect(reverse('welcome'))
    else:
        return render(request, "profile.html")


def hr(request):
    return render(request, "hr.html")


def it(request):
    return render(request, "it.html")


def emp(request):
    return render(request, "employee.html")
