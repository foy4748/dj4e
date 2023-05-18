from django.urls import path

from . import views

app_name = "cats"
urlpatterns = [
    path('', views.CatList.as_view(), name='cats'),
    #path('main/create/', views.CatCreate.as_view(), name='cat_create'),
    #path('main/<int:pk>/update/', views.CatUpdate.as_view(), name='cat_update'),
]
