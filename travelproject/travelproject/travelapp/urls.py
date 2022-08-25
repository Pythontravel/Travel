
from django.urls import path

import travelapp

from . import views

urlpatterns = [
    path('',views.demo,name='demo')
    #path('about/',views.about,name='about'),
    #path('contact',views.contact,name='contact'),
    #path('demo1',views.demo1,name='demo1'),
    #path('operators/',views.operators,name='operators')
]
