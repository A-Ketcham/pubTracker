from django.conf.urls import include, url
from . import views

urlpatterns = [
	# URL patterns for login/logout
	url('^', include('django.contrib.auth.urls')),
	# ex: /forms/
    url(r'^$', views.index, name='index'),
	# ex: /forms/cadet/
	url(r'^plans/$', views.plans, name='plans'),
	url(r'^help/$', views.help, name='help'),
	# ex: /forms/cadet/travel2
	url(r'^(?P<xNumber>[0-9]+)/travel(?P<travelID>[0-9]+)/$', views.update, name='update'),
]