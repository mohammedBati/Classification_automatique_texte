from django.shortcuts import render , redirect
from django.shortcuts import get_object_or_404
import sys
from subprocess import run,PIPE
import subprocess
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required
# Create your views here.

from .models import *
from .forms import CreateUserForm
import pyautogui

#from .filters import OrderFilter

# Create your views here.

def registerPage(request):
	if request.user.is_authenticated:
		return redirect('/')
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Account was created for ' + user)

				return redirect('/login')


		context = {'form':form}
		return render(request, 'register.html', context)

def loginPage(request):
	if request.user.is_authenticated:
		return redirect('/index')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('/index')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('/login')

def home(response):
    return render(response, "main/home.html", {})


from django.views.generic import TemplateView, ListView, CreateView
from django.core.files.storage import FileSystemStorage
from django.urls import reverse_lazy

from .forms import BookForm , UploadFileForm
from .models import Book
import os
from django.conf import settings


@login_required(login_url='/login')
def inde(request):
     context = {}
     if request.method == 'POST':
        uploaded_file = request.FILES['fl']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        file_path=os.path.join(settings.MEDIA_ROOT,name)
        fh=open(file_path,'rb')
        f=fh.read().decode()
        fh.close()
        #out= run([sys.executable,'KNN.py',f],shell=False,stdout=PIPE)
        context={'url':name ,
		         #'data1':out.stdout.decode(),
                 'data1':uploaded_file,
				  'data2':f }
     return render(request, 'main/index.html', context)


def index(request):
    context = {}
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
           form.save()
           context={'data1':"valider",
		             'form':form}
           return render(request, 'main/index.html', context)
    else:
        form = BookForm()
    return render(request, 'main/index.html',{
        'form': form })

def calassifier(request):
	context={}
	if request.method == 'POST':
		if request.POST.get('param'):
			return classifier_text(request)
		else :
		    return upload_multiple_files(request)
	else:
			form = UploadFileForm()
	return render(request, 'main/index.html', {'form': form})


def classifier_text(request):
     context={}
     if request.method == 'POST':
         inp = request.POST.get('param')
         model=request.POST.get('sel')
         md=teste_module(model)
         out = run([sys.executable,md,inp],shell=False,stdout=PIPE)
         categori=out.stdout.decode()
         affi_ca="la catégorie de texte est :" + " " +'" ' + categori + '"' +  " d'après le "+ " " + model
         context = {'data2':affi_ca}
         return render(request, 'main/index.html', context)

     else:
         form = UploadFileForm()
     return render(request, 'main/index.html', {'form': form})


def upload_multiple_files(request):
    context={}
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        files = request.FILES.getlist('files')
        model=request.POST.get('sel')
        md=teste_module(model)
        if form.is_valid():
            categs=[]
            for f in files:
                handle_uploaded_file(f)
                name=f.name
                file_path=os.path.join(settings.MEDIA_ROOT,name)
                fh=open(file_path,'rb')
                f=fh.read().decode()
                fh.close()
                out= run([sys.executable,md,f],shell=False,stdout=PIPE)
                categ=out.stdout.decode()
                nm_categ="la catégorie de " + " " + name + " est : " + categ + " d'après le Model" + "(" + model + ")"
                categs.append(nm_categ)
            context = {'data1' : categs,
			              'form':form}
            return render(request, "main/index.html", context)
    else:
        form = UploadFileForm()
    return render(request, 'main/index.html', {'form': form})


def handle_uploaded_file(f):
    with open('media/'+f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def teste_module(module):
    if module == "Naive Bayes":
       return "NVB.py"
    else :
       if module == "K-NN":
           return "KNN.py"
       else :
           if module =="SVM" :
              return "SVM.py"
           else :
              if module == "Logistic Regression":
                 return "LogisticRegrression.py"
