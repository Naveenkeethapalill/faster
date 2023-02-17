from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('about',views.about,name='about'),
    path('order',views.order,name='order'),
    path('myorders',views.myorders,name='myorders'),
    path('service',views.service,name='service'),
    path('contact',views.contact,name='contact'),
    path('create',views.create,name='create'), 
]


