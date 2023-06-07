from django.shortcuts import render
from .models import Person

# Create your views here.
def startpage(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        age = request.POST.get("age")
        height = request.POST.get("height")
        person = Person(name=name, age=age, height=height)
        person.save()
        print(person)
    return render(request, "crud/startpage.html")

def loginUser(request):
    return render(request, "crud/login_user.html")

def registerUser(request):
    return render(request, "crud/register_user.html")

def printData(request):
    persons = Person.objects.all()
    return render(request, "crud/register_user.html", {"persons": persons})
