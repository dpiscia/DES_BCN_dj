from django.conf.urls import patterns, url

from registration import views

urlpatterns = patterns('',
    url(r'^home', views.index, name='index'),
    url(r'^registration', views.index, name='registration')
)