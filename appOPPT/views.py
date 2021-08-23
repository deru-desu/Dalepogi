from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import StudentInfo, UpdateInfo, CreateUserForm
from appOPPT.models import information, UpdateInfo
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

#LOGIN AND REGISTER ADMIN

def registerPage(request):
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Account was created for ' + user)

				return redirect('login')
			

		context = {'form':form}
		return render(request, 'registeradmin.html', context)

def loginPage(request):
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('readadmin')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'login.html', context)

#LOGOUT ADMIN

def logoutUser(request):
	logout(request)
	return redirect('login')

#READ FOR ADMIN

@login_required(login_url='login')
def listadmin(request):
    stulist = information.objects.all()
    context = {'stulist':stulist}
    return render(request, 'list admin.html', context)

@login_required(login_url='login')
def searchadmin(request):
    if request.method == 'GET':
        search = request.GET.get('search')
        post = information.objects.all().filter(studentID=search)
        context = {'post':post}
        return render(request, 'searchresult admin.html', context)


#CREATE/REGISTER

def registration(request):
    form = StudentInfo()
    if request.method == 'POST':
        form = StudentInfo(request.POST)
        if  form.is_valid():
            form.save()
            return redirect('/')
    context = {'form':form}
    return render(request, 'register.html', context)

#READ

def list(request):
    stulist = information.objects.all()
    context = {'stulist':stulist}
    return render(request, 'list.html', context)

def search(request):
    if request.method == 'GET':
        search = request.GET.get('search')
        post = information.objects.all().filter(studentID=search)
        context = {'post':post}
        return render(request, 'searchresult.html', context)

#UPDATE/EDIT

def UpdateInfo(request, pk):
    student = information.objects.get(id=pk)
    form = StudentInfo(instance=student)
    if request.method == 'POST':
        form = StudentInfo(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('read')
    context = {'form':form}
    return render(request, 'register.html', context)

#DELETE

#def delete(request, id):
    #info = information.objects.get(id=id)
   # info.delete()
   # return redirect('/')

# Create your views here.
