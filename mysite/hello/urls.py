from django.urls import path
#from django.views.generic.base import TemplateView
from . import views


app_name = "hello"
urlpatterns = [
        path("", views.myview, name="hello"),
]


