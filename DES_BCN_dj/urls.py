from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
from registration.views import index, registration, form_prova

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'DES_BCN_dj.views.home', name='home'),
    # url(r'^DES_BCN_dj/', include('DES_BCN_dj.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^reg', include('registration.views.index')),
    url(r'^home/', index, name='index'),
    url(r'^registration', registration, name='registration'),
    url(r'^prova', form_prova, name='form_prova'),


)
