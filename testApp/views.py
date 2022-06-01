from django.conf import UserSettingsHolder
from django.shortcuts import render, redirect, get_object_or_404
from .forms import UsersForm
from django.views.generic import ListView, DetailView

from .models import Users


def index(request):
    users = Users.objects.all()
    return render(request, "testapp/index.html", {"users": users})
