from django.http import HttpResponse
from django.forms import ModelForm
from registration.models import User
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django import forms
from django.conf.urls import url
from django.core.urlresolvers import reverse

from djangomako.shortcuts import render_to_response, render_to_string
from forms import MessageForm

def index(request):
    #return render_to_response('home.mako', {'tab' : 'home'} )
    return render(request, 'home.mako')
# Create your views here.
def registration(request):
    
    
    #return render_to_response('home.mako', {'tab' : 'home'} )
    return render(request, 'registration.mako')
    
def form_prova(request):
    # This view is missing all form handling logic for simplicity of the example
    return render(request, 'form_prova.html', {'form': MessageForm()})