from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import redirect, render,HttpResponseRedirect
from .forms import StudentRegistration
from .models import User
# Create your views here.

#function for adding and saving details
def add_show(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            fm.save()
            fm =StudentRegistration()
    else:
        fm =StudentRegistration()
    std = User.objects.all()
    return render(request,'add&show.html',{'form':fm,'std':std})

#deleting details by using id
def delete_detail(request,id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')
    
#Editing details by id

def edit(request,id):
    if request.method == "POST":
        ei = User.objects.get(pk=id)
        fm = StudentRegistration(request.POST,instance=ei)
        if fm.is_valid():
            fm.save()
        return HttpResponseRedirect('/')
    else:
        ei = User.objects.get(pk=id)
        fm = StudentRegistration(instance=ei)
    return render(request,'update.html',{'form':fm})

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        old = User.objects.all().values()
        for member in old:
            if username == member['email'] and password == member['password']:
                return redirect('add_show')
            else:
                HttpResponse('Bad Credential!!')
            print(member['email'])
            print(member['password'])
    return render(request,'login.html')