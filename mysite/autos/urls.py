from django.urls import path

from . import views

app_name = "autos"
urlpatterns = [
        path("", views.AutoView.as_view(), name="autos"),
        path("/create", views.AutoCreateView.as_view(), name="autos-create"),
]
