from django.shortcuts import render,redirect
from django.http import HttpResponse
# import data form model
from myapp.models import Person
from django.contrib import messages

# Create your views here.
def index(request):
    all_person = Person.objects.all()
    # all_person = Person.objects.filter(age=25)
    return render(request,"index.html",{"all_person":all_person})

def about(request):
    return render(request,"about.html")

def form(request):
    if request.method == "POST":
        name = request.POST["name"]
        age  = request.POST["age"]
        person = Person.objects.create(
            name = name,
            age  = age
        )
        person.save()
        messages.success(request,"Data recorded")
        return redirect("/")
    else:
        return render(request,"form.html")

def edit(request,person_id):
    print("-> Pushed update botton")
    if request.method == "POST":
        person = Person.objects.get(id=person_id)
        person.name = request.POST["name"]
        person.age  = request.POST["age"]
        person.save()
        messages.success(request,"Updated data!")
        return redirect("/")
    else:
        person = Person.objects.get(id=person_id)
        return render(request,"edit.html",{"person":person})
    
def delete(request,person_id):
    person = Person.objects.get(id=person_id)
    person.delete()
    messages.success(request,"Updated data!")
    return redirect("/")