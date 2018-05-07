from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.core.urlresolvers import reverse

# Create your views here.
def index(request):
	return HttpResponse("django")

def fun(request,num,name):
	return HttpResponse("fun....%s %s"%(num,name))

def fun2(request):
	return redirect(reverse('index'))