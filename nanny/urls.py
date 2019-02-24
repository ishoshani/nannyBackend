from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('parentSignUp', views.parentSignUp, name='parentSignUp'),
    path('parentProcess', views.parentProcess, name = 'parentProcess'),
    path('nannySignUp', views.nannySignUp, name = 'nannySignUp'),
    path('nannyProcess', views.nannyProcess, name = 'nannyProcess'),
    path('nanny/done', views.done, name = 'done'),
]
