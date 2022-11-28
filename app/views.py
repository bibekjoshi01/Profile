from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import Profile
from . forms import *

def profile(request):
    details = Profile.objects.get(id=3)
    context = {
        'profile':details,
    }
    return render(request, 'app/profile.html', context)

def edit_profile(request):
    user = Profile.objects.get(id=3)
    form = Profile_Form(instance=user)

    if request.method == 'POST':
        form = Profile_Form(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('/')
    context ={
        'form':form,

    }
    return render(request, 'app/edit_profile.html', context)

