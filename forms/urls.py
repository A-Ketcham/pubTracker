from django.conf.urls import url

from . import views

urlpatterns = [
	# ex: /forms/
    url(r'^$', views.index, name='index'),
	# ex: /forms/cadet/
	url(r'^(?P<xNumber>[0-9]+)/$', views.cadet, name='cadet'),
]