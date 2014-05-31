from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'^$', 'admin.views.index'),
	url(r'^index$', 'admin.views.index'),
	url(r'^login$', 'admin.views.login'),
)