
from helloworld import views
from django.urls import path

urlpatterns = [
    path('', views.helloworld, name="helloworld")
]
