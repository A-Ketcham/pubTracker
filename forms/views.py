from django.shortcuts import get_object_or_404, render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone
from django.template import Context, RequestContext, loader

from .models import TravelPlan, UserProfile, ZIP
from django.contrib.auth.models import User

from django.forms import ModelForm

from django.contrib.auth.decorators import login_required

def index(request):
	user = User.objects.filter()[:1]
	details = UserProfile.objects.filter()[:1]
	return render_to_response('forms/index.html', {'User': user, 'Details': details}, RequestContext(request))
	
def profile(request):
	zips = ZIP.objects.all()
	t = loader.get_template('forms/index.html')
	c = Context({'object_list': zips})
	return HttpResponse(t.render(c))

def plans(request):
	plans = TravelPlan.objects.all()
	t = loader.get_template('forms/plans.html')
	c = Context({'Plans': plans})
	return HttpResponse(t.render(c))
	
def help(request):
	zips = ZIP.objects.all()
	t = loader.get_template('forms/help.html')
	c = Context({'object_list': zips})
	return HttpResponse(t.render(c))

#def insert(request):
#    return HttpResponse("This is where you can create records")

def update(request, travelID):
	return HttpResponse("Edit travel plan" % travelID)
	
#def delete(request):
#	return HttpResponse("This is where you can delete records")