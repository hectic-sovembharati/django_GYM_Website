from django.shortcuts import render, HttpResponse

from .models import About, Home, Members
from django.contrib import messages

# Create your views here.
def index(request):
    
    data = About.objects.all()
    abt = {
        "about_number": data
        
    }
    
    
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        num = request.POST.get('num')
        msg = request.POST.get('msg')
        members = Members(name=name, email=email, num=num, msg=msg)
        members.save()
        messages.success(request, 'Your message has been sent!')
    return render(request, 'index.html',abt)
    # return HttpResponse("this is homepage")


 