from django.shortcuts import render, redirect
from .models import *
from .forms import *


def home(request):
    developers = Developer.objects.all()
    for d in developers:
        d.getScore()
    return render(request, 'developers.html', {'developers': developers})


def edit(request, id):
    instance = Developer.objects.get(pk=id)
    if request.method == "POST":
        fm = DevelopersForm(request.POST, instance=instance)
        if fm.is_valid:
            fm.save()
            return redirect('developers')
    fm = DevelopersForm(instance=instance)
    return render(request, "edit.html", {'fm': fm})


def add(request):
    context = {}
    form = DevelopersForm(request.POST)
    if request.method == "POST":
        if form.is_valid:
            form.save()
            return redirect('developers')
    context['fm'] = form
    return render(request, "edit.html", context)


def delete(request, id):
    developers = Developer.objects.get(pk=id).delete()
    return redirect('developers')

def search(request):
  
    technologies = Technology.objects.all()
    domains = Domain.objects.all()
    locations = []
    for developer in Developer.objects.all():
        if developer.location not in locations:
            locations.append(developer.location)

    developers = {}    

    if request.method == 'POST': 
        getLocation=request.POST.get('location', 'defaultvalue')
        getTechnology=request.POST.get('technology', 'defaultvalue')
        getDomain=request.POST.get('domain', 'defaultvalue')
        print(getLocation,getTechnology,getDomain)

        if(getLocation != 'defaultvalue'):
            print("if 1")
            developers = Developer.objects.filter(
                location=getLocation
            )
            if(getTechnology != 'defaultvalue'):
                print("if 1 and 2")
                developers = Developer.objects.filter(
                    location=getLocation,
                    technology__name=getTechnology
                )
                print("======developers",developers)
                if(getDomain != 'defaultvalue'):
                    print("if 1 ,2 and 3")
                    developers = Developer.objects.filter(
                        location=getLocation,
                        technology__name=getTechnology,
                        domain__name=getDomain
                    )
            elif(getDomain != 'defaultvalue'):
                print("if 1 and 3")
                developers = Developer.objects.filter(
                    location=getLocation,
                    domain__name=getDomain
                )

        elif(getTechnology != 'defaultvalue'):
            print("if 2")
            developers = Developer.objects.filter(
                technology__name=getTechnology
            )
            if(getDomain != 'defaultvalue'):
                print("if 2 and 3")
                developers = Developer.objects.filter(
                    technology__name=getTechnology,
                    domain__name=getDomain
                )
        elif(getDomain != 'defaultvalue'):
            print("if 3")
            developers = Developer.objects.filter(
                domain__name=getDomain
            )
        else:
            developers = {}       

    return render(request, 'search.html', {'locations': locations, 'technologies': technologies, 'domains': domains, 'developers': developers,'noOfRecords':len(developers)})

def details(request, id):
    developers = Developer.objects.filter(id=id)
    return render(request, 'developers.html', {'developers': developers})


def weightage(request):
    instance = Weightage.objects.get(pk=1)
    if request.method == "POST":
        fm = WeightageForm(request.POST, instance=instance)
        if fm.is_valid:
            fm.save()
            return redirect('developers')
    fm = WeightageForm(instance=instance)
    return render(request, "weightage.html", {'fm': fm})
