from django.urls import path
from . import views

appname='chatting'
urlpatterns = [
    path('index/',views.index),
]