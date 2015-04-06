from models import *
from form import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
import socket
from extend_user.models import ServerLogin
from django.contrib.auth.models import User


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

def complete(request):
    return render(request, 'complete.html')

