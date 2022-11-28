from django.shortcuts import render
from django.http import HttpResponse
from . models import Profile

def profile(request):
    details = Profile.objects.get(id=1)
    context = {
        'profile':details,
    }
    return render(request, 'app/profile.html', context)
