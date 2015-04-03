from models import *
from form import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
import socket

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/complete/")
    else:
        form = UserCreationForm()
    return render(request, "register.html", {
        'form': form,
    })

def complete(request):
    return render(request, 'complete.html')

