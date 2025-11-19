from django.shortcuts import render
from .models import Update

def update_list(request):
    # Fetch all updates, ordered by newest first
    updates = Update.objects.all().order_by('-timestamp')
    return render(request, 'updates/update_list.html', {'updates': updates})
