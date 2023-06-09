from django.urls import path, reverse_lazy
from . import views

app_name='solo'

urlpatterns = [
        path('', views.SoloView.as_view(), name="solo"),
]
