from django.shortcuts import render
from .models import Gallery,Contact
from django.http import HttpResponse

# Create your views here.
# go to home page


def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")


def menu(request):
    return render(request, "menu.html")

def gallery(request):
    gallery_pics= Gallery.objects.all()
    return render(request, "gallery.html", {'gallery':gallery_pics})

def contact(request):
    if request.method == "POST":
        name= request.POST.get("name")
        email=request.POST.get("email")
        subject=request.POST.get("subject")
        message=request.POST.get("message")

        contact_info=Contact(name=name,email=email,subject=subject,message=message)
        contact_info.save()
    return render(request, "contact.html")
    return HttpResponse('message sent sucessfully')
