from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
	return render(request, 'proxy/home.html')

@login_required
def secret(request):
	return render(request, 'proxy/index.html', {'title':'Secret'})

