from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from rest_framework import generics
from .serializers import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter


# Create your views here.

class UserListView(generics.ListAPIView):
    serializer_class = UsersSerializer
    queryset = Users.objects.all()
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filter_fields = ('Is_Active', 'Aadhar_Number', 'user_id')
    ordering_fields = ('Is_Active', 'Full_Name', 'user_id')
    search_fields = ('Full_Name', 'user_id', 'city')

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('user_list')
    else:
        form = UserCreationForm()
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for '+ user)
                return redirect('login')

        context={'form':form}
        return render(request, 'aui/register.html', context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('user_list')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('user_list')
            else:
                messages.info(request, 'Username or Password is incorrect')
        context={}
        return render(request, 'aui/login.html', context)