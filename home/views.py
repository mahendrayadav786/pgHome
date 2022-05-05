from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
def home(request):
    return render(request, "home/home.html")


def sell(request):
    return render(request, "home/addpg.html")



def contact(request):
    return render(request, "home/contact.html")
def about(request):
    return render(request, "home/aboutus.html")


def addpg(request):

         if request.method == "POST":
             pgname = request.POST.get("Pgname")
             contact = request.POST.get("Contact")
             address = request.POST.get("Address")
             state = request.POST.get("State")
             zip = request.POST.get("Zip")

             print(pgname, contact, address, state, zip)

             return redirect("/")
         return redirect("/")
     
     
def rent(request):
        return render(request, "home/rent.html")
    
     
     
