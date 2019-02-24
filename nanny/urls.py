from django.urls import path

from . import views
import logging
from django.conf.urls import url, include
from django.contrib.auth.models import User
from .models import Host,Nanny,Schedule,Note
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import serializers, viewsets, routers

# Serializers define the API representation.
class HostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Host
        fields = ('url','username','phone','location','kids','password')

class NannySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Nanny
        fields = ('url','username','phone','location','price','password')

class ScheduleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Schedule
        fields = ('host_id','nanny_id','time','payment')
class NoteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Note
        fields = ('host_id', 'nanny_id', 'text')


# ViewSets define the view behavior.


class HostViewSet(viewsets.ModelViewSet):
    queryset = Host.objects.all()
    serializer_class = HostSerializer


class NannyViewSet(viewsets.ModelViewSet):
    queryset = Nanny.objects.all()
    serializer_class=NannySerializer

class ScheduleViewSet(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class=ScheduleSerializer

class ScheduleHostSet(viewsets.ModelViewSet):
    serializer_class =ScheduleSerializer
    def get_queryset(self):
        data = self.request.query_params['host']
        return Schedule.objects.filter(host = data)

class ScheduleNannySet(viewsets.ModelViewSet):
    serializer_class =ScheduleSerializer
    def get_queryset(self):
        data = self.request.query_params['nanny']
        return Schedule.objects.filter(nanny = data)

class NoteViewSet(viewsets.ModelViewSet):
    serializer_class=NoteSerializer
    def get_queryset(self):
        data = self.request.query_params
        if('host' in data):
            host = data['host']
            return Note.objects.filter(host = host)
        if('nanny' in data):
            nanny = data['nanny']
            return Note.objects.filter(nanny= nanny)


# Routers provide a way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'hosts',HostViewSet)
router.register(r'nannys',NannyViewSet)
router.register(r'schedules',ScheduleViewSet)
router.register(r'hostschedules',ScheduleHostSet,basename = "hostSched")
router.register(r'nannyschedules',ScheduleNannySet,basename = "nannySched")
router.register(r'notes',NoteViewSet,basename = "notes")


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', views.index, name='index'),
    path('parentSignUp', views.parentSignUp, name='parentSignUp'),
    path('parentProcess', views.parentProcess, name = 'parentProcess'),
    path('nannySignUp', views.nannySignUp, name = 'nannySignUp'),
    path('nannyProcess', views.nannyProcess, name = 'nannyProcess'),
    path('nanny/done', views.done, name = 'done'),

]
