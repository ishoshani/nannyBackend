from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Host



def index(request):
    template = loader.get_template('nanny/index.html')
    context = {}
    return HttpResponse(template.render(context, request))
def parentSignUp(request):
    template = loader.get_template('nanny/parentSignUp.html')
    context = {}
    return HttpResponse(template.render(context, request))
def parentDone(request):
    info = {
    "username" : request.POST["user_name"],
    "first name" :  request.POST["first"],
    "last name" : request.POST["last"],
    "phone" : request.POST["phone"],
    "password" : request.POST["password"],
    "location" : ""+request.POST["street"]+" "+request.POST["street2"]+", "+request.POST["city"]+", "+request.POST["state"]
    }

    Host.objects.create(**info);
    return HttpResponseRedirect(index)




def nannySignUp(request):
    template = loader.get_template('nanny/nannySignUp.html')
    context = {}
    return HttpResponse(template.render(context, request))





# Create your views here.
