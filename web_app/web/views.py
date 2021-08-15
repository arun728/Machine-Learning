from django.shortcuts import render
from django.http import HttpResponse

def home(request):
	return HttpResponse('<h1>Click to view the Top Secret!</h1>')

def secret(request):
	return HttpResponse('<h2>These are the droids you are looking for!</h2>')
