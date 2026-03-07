from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('viewblog/<str:pk>',views.blogs,name='viewblog'),
]