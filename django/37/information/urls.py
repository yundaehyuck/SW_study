from django.urls import path
from . import views

appname = 'information'
urlpatterns = [
    path('index/',views.index),
]