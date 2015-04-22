from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone
from django.template import Context, RequestContext, loader

from .models import TravelPlan, UserProfile, ZIP

from django.forms import ModelForm

from django.contrib.auth.decorators import login_required

def index(request):
	zips = ZIP.objects.all()
	t = loader.get_template('forms/index.html')
	c = Context({'object_list': zips})
	return HttpResponse(t.render(c))
	
def profile(request):
	zips = ZIP.objects.all()
	t = loader.get_template('forms/index.html')
	c = Context({'object_list': zips})
	return HttpResponse(t.render(c))

def plans(request):
	zips = ZIP.objects.all()
	t = loader.get_template('forms/plans.html')
	c = Context({'object_list': zips})
	return HttpResponse(t.render(c))
	
def help(request):
	zips = ZIP.objects.all()
	t = loader.get_template('forms/plans.html')
	c = Context({'object_list': zips})
	return HttpResponse(t.render(c))

#def insert(request):
#    return HttpResponse("This is where you can create records")

def update(request, travelID):
	return HttpResponse("Edit travel plan" % travelID)
	
#def delete(request):
#	return HttpResponse("This is where you can delete records")