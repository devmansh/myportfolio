# profile/views.py

from django.shortcuts import render, redirect
from .models import Project, Profile
from .forms import ContactForm

def home(request):
    profile = Profile.objects.first()
    return render(request, 'profile/home.html', {'profile': profile})

def projects(request):
    projects = Project.objects.all()
    return render(request, 'profile/projects.html', {'projects': projects})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_success')
    else:
        form = ContactForm()
    return render(request, 'profile/contact.html', {'form': form})

def contact_success(request):
    return render(request, 'profile/contact_success.html')
