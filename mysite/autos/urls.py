from django.urls import path

from . import views

app_name = "autos"
urlpatterns = [
        path("", views.AutoView.as_view(), name="autos"),
        path("auto-create/", views.AutoCreateView.as_view(), name="auto-create"),
        path("make-create/", views.MakeCreateView.as_view(), name="make-create"),

        path("<int:pk>/auto-update", views.AutoUpdateView.as_view(), name="auto-update"),
        path("<int:pk>/make-update", views.MakeUpdateView.as_view(), name="make-update"),

        path("<int:pk>/auto-delete", views.AutoDeleteView.as_view(), name="auto-delete"),
        path("<int:pk>/make-delete", views.MakeDeleteView.as_view(), name="make-delete"),
        
]
