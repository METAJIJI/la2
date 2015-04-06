from models import Accounts
from form import UserCreationForm, ChangePasswordForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
import socket
from extend_user.models import ServerLogin
from django.contrib.auth.models import User
import whirlpool
import base64
import hashlib
from la2.settings import hash_type



def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            login = ServerLogin(user_id=request.user.id, login=form.cleaned_data['login'])
            login.save(using='default')
            form.save()
            return HttpResponseRedirect("/complete/")
    else:
        form = UserCreationForm()
    return render(request, "register.html", {
        'form': form,
    })


def change_password(request, login):
    login = login[:-1]
    acc = Accounts.objects.get(login=login)
    if request.method == 'POST':

        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            password = request.POST.get('password1', '')
            oldpass = request.POST.get('oldpassword', '')
            if hash_type == 'whirlpool':
                password = base64.b64encode(whirlpool.new(password).digest())
                if acc.password == base64.b64encode(whirlpool.new(oldpass).digest()):
                    acc_obj = Accounts(login=login, password=password)
                    acc_obj.save()
                    return HttpResponseRedirect("/changed/")
            elif hash_type == 'sha1':
                password = base64.b64encode(hashlib.sha1(password).digest())
                if acc.password == base64.b64encode(hashlib.sha1(oldpass).digest()):
                    acc_obj = Accounts(login=login, password=password)
                    acc_obj.save()

                    return HttpResponseRedirect("/changed/")
            return render(request, "change.html", {
        'form': form, 'acc': acc,
    })
    else:
        form = ChangePasswordForm()
    return render(request, "change.html", {
        'form': form, 'acc': acc,
    })


def complete(request):
    return render(request, 'complete.html')

def changed(request):
    return render(request, 'changed.html')

def cabinet(request):
    query = ServerLogin.objects.using('default').filter(user_id=request.user.id)

    return render(request, "cabinet.html", {
        'query': query,
    })

