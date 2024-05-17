from django.shortcuts import render
from .models import Profile

def profile_view(request):
    profile = Profile.objects.first()
    return render(request, 'profile.html', {'profile': profile})

