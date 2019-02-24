from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('parentSignUp', views.parentSignUp, name='parentSignUp'),
    path('nannySignUp', views.nannySignUp, name = 'nannySignUp'),
    path('parentDone', views.parentDone, name = 'parentDone')
]
