from django.conf.urls import url

from . import views

app_name = 'hades'

urlpatterns = [
	url(r'^$', views.index, name='index'),

	url(r'^signup$', views.signup, name='signup'),
	url(r'^signup/$', views.signup, name='signup'),

	url(r'^login$', views.doLogin, name='login'),
	url(r'^login/$', views.doLogin, name='login'),

	url(r'^logout$', views.doLogout, name='logout'),
	url(r'^logout/$', views.doLogout, name='logout'),

	url(r'^blog$', views.blog, name='blog'),
	url(r'^blog/$', views.blog , name='blog'),
	url(r'^blog/(?P<page>[0-9]+)$', views.blog, name='blog'),

	url(r'^video$', views.video, name='video'),
	url(r'^video/$', views.video, name='video'),
	url(r'^video/(?P<showName>.+)$', views.video, name='show'),

	url(r'^sudoku$', views.sudoku, name='sudoku'),
	url(r'^sudoku/$', views.sudoku, name='sudoku'),

	url(r'^.+$', views.notFound, name='notFound'),
]
