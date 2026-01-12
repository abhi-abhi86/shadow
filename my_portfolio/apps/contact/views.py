from django.shortcuts import render
from django.http import JsonResponse

def contact(request):
    if request.method == 'POST' and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        # Simulate form processing or add actual logic here
        # form = ContactForm(request.POST)
        # if form.is_valid(): form.save()
        return JsonResponse({'status': 'success', 'message': 'Message sent successfully!'})
    return render(request, 'contact/contact.html')
