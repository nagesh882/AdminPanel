from django.shortcuts import render,redirect
from service.models import User
# Create your views here.

def home(request):
    context = User.objects.all().order_by("id")[:]
    # context = User.objects.all().order_by("id")
    # context = User.objects.all().order_by("-id")
    data = {
        "context":context,
    }
    return render(request, 'index.html', data)

def save(request):
    if request.method=="POST":
        userName = request.POST.get("name")
        userSurname = request.POST.get("surname")
        userPhone = request.POST.get("phone")
        userEmail = request.POST.get("email")
        userAddress = request.POST.get("address")

        e = User(
            userName = userName,
            userSurname = userSurname,
            userPhone = userPhone,
            userEmail = userEmail,
            userAddress = userAddress,
            
        )
        e.save()
        return redirect('homePage')
    return render(request, 'home.html')











def update(request,id):
    if request.method=="POST":
        userName = request.POST.get("name")
        userSurname = request.POST.get("surname")
        userPhone = request.POST.get("phone")
        userEmail = request.POST.get("email")
        userAddress = request.POST.get("address")

        e = User(
            id = id,
            userName = userName,
            userSurname = userSurname,
            userPhone = userPhone,
            userEmail = userEmail,
            userAddress = userAddress,
            
        )
        e.save()
        return redirect('homePage')
    return render(request, 'update.html')


def Delete(request, id):
    e = User.objects.filter(id = id)
    
    e.delete()
    
    context = {
        'e':e,
    }
    return redirect('homePage')



def EDIT(request):

    e = User.objects.all()

    e = {

        'e':e,
    
    }

    return render(request, 'update.html', e)
