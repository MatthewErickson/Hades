from django.conf.urls import url

from . import views

app_name = 'hades'

urlpatterns = [
	url(r'^$', views.index, name='index'),

	url(r'^blog$', views.blog, name='blog'),
	url(r'^blog/$', views.blog , name='blog'),
	url(r'^blog/(?P<page>[0-9]+)$', views.blog, name='blog'),

	url(r'^.+$', views.notFound, name='notFound'),
]
