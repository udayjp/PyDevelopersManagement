from django.shortcuts import render,redirect
from .models import *
from .forms import *

def home(request):
	developers=Developer.objects.all() 
	for d in developers:
		d.getScore()
	return render(request,'developers.html',{'developers':developers})

def edit(request,id):
	instance  =  Developer.objects.get(pk=id)
	if request.method=="POST":
		fm=DevelopersForm(request.POST,instance=instance)
		if fm.is_valid:
			fm.save()
			return redirect('developers')
	fm=DevelopersForm(instance=instance)
	return render(request,"edit.html",{'fm':fm})

def add(request):
	context ={}	
	form=DevelopersForm(request.POST)
	if request.method=="POST":		
		if form.is_valid:
			form.save()
			return redirect('developers')
	context['fm']= form
	return render(request, "edit.html", context)   

def delete(request,id):
	developers=Developer.objects.get(pk=id).delete()
	return redirect('developers')

def fillsearch():
	developers=Developer.objects.all()	
	technologies=Technology.objects.all()
	domains=Domain.objects.all()
	locations=[]
	for developer in developers:
		if developer.location not in locations:
			locations.append(developer.location)
	return locations,technologies,domains

def search(request):
	locations=fillsearch()[0]
	technologies=fillsearch()[1]
	domains=fillsearch()[2]			
	return render(request,'search.html',{'locations':locations,'technologies':technologies,'domains':domains})

def searchResult(request,searchby,txt):	
	locations=fillsearch()[0]
	technologies=fillsearch()[1]
	domains=fillsearch()[2]

	if searchby=='location':
		developers=Developer.objects.filter(location__contains=txt)
	elif searchby=='technology':
		developersId=[]
		for developer in Developer.objects.all():
			for dev in developer.technology.all():
				if dev.name == txt and developer.id not in developersId:
					developersId.append(developer.id)
					break
		developers=Developer.objects.filter(id__in=developersId)
	elif searchby=='domain':	
		developersId=[]
		for developer in Developer.objects.all():
			for dev in developer.domain.all():
				if dev.name == txt and developer.id not in developersId:
					developersId.append(developer.id)
					break
		developers=Developer.objects.filter(id__in=developersId)
	else:
		developers=Developer.objects.filter(location__contains='Pune')

	return render(request,'search.html',{'locations':locations,'technologies':technologies,'domains':domains,'developers':developers})

def details(request,id):
	developers=Developer.objects.filter(id=id)
	return render(request,'developers.html',{'developers':developers})

def weightage(request):
	instance  = Weightage.objects.get(pk=1)
	if request.method=="POST":
		fm=WeightageForm(request.POST,instance=instance)
		if fm.is_valid:
			fm.save()
			return redirect('developers')
	fm=WeightageForm(instance=instance)
	return render(request,"weightage.html",{'fm':fm})