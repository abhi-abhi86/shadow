from django.shortcuts import render
from .models import Skill

def home(request):
    skills = Skill.objects.all()
    # Optional: You might want to pre-group them here or just pass all
    context = {
        'skills': skills,
    }
    return render(request, 'core/home.html', context)

def projects(request):
    return render(request, 'core/projects.html')

def disease_predictor_detail(request):
    return render(request, 'core/disease_predictor_detail.html')

def spiffy_detail(request):
    return render(request, 'core/spiffy_detail.html')

def shadow_detail(request):
    return render(request, 'core/shadow_detail.html')
