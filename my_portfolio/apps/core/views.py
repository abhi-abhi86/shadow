from django.shortcuts import render

def home(request):
    return render(request, 'core/home.html')

def projects(request):
    return render(request, 'core/projects.html')

def disease_predictor_detail(request):
    return render(request, 'core/disease_predictor_detail.html')

def spiffy_detail(request):
    return render(request, 'core/spiffy_detail.html')

def shadow_detail(request):
    return render(request, 'core/shadow_detail.html')
