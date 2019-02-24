from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.urls import reverse


from .models import Host



def index(request):
    template = loader.get_template('nanny/index.html')
    context = {}
    return HttpResponse(template.render(context, request))
def parentSignUp(request):
    template = loader.get_template('nanny/parentSignUp.html')
    context = {}
    return HttpResponse(template.render(context, request))
def parentProcess(request):
    info = {
    "username" : request.POST["user_name"],
    "first_name" :  request.POST["first"],
    "last_name" : request.POST["last"],
    "phone" : request.POST["phone"],
    "password" : request.POST["password"],
    "location" : ""+request.POST["street"]+" "+request.POST["street2"]+", "+request.POST["city"]+", "+request.POST["state"]
    }

    id = Host.objects.create(**info);
    return HttpResponseRedirect("nanny/parentDone")

def parentDone(request):
    return render(request, 'nanny/ParentDone.html', {})

def nannySignUp(request):
    template = loader.get_template('nanny/nannySignUp.html')
    context = {}
    return HttpResponse(template.render(context, request))





# Create your views here.
