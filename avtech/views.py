from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView

from .forms import ThinkForm,VideoForm
from .models import Think,Video

# Create your views here.
def home_view(request, *args, **kwargs):
	count = User.objects.count()
	return render(request, "home.html", {
		'count': count
	})

def signup(request):
	if request.method == "POST":
		form = UserCreationForm(request.POST)
		if form.is_valid():
			user = form.save()
			return redirect('home')
	else:
		form = UserCreationForm()
	return render(request, "registration/signup.html",{
			'form' : form 
		})

def about_view(request, *args, **kwargs):
	return render(request, "about.html", {})

def think(request):
	thoughts = Think.objects.all()
	return render(request, "think.html", {
		'thoughts' : thoughts
		})

def think_ideas(request):
	if request.method == 'POST':
		form = ThinkForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('think')
	else:
		form = ThinkForm()
	return render(request, "think_ideas.html", {
		'form': form

	})



def innovate_view(request, *args, **kwargs):
	return render(request, "innovate.html", {})


def advisor_view(request, *args, **kwargs):
	return render(request, "advisor.html", {})

def tunnel_view(request, *args, **kwargs):
	return render(request, "tunnel.html", {})


def upload(request):
	if request.method == 'POST':
		form = VideoForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('innovate')
	else:
		form = VideoForm()
	context= {'videofile': videofile,
              'form': form
              }
	return render(request, "upload.html", context)
	