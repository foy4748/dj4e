from django.urls import path, reverse_lazy
from . import views

app_name='ads'
urlpatterns = [
    path('', views.AdListView.as_view(), name='ads'),
    path('ad/<int:pk>', views.AdDetailView.as_view(), name='ad_detail'),
    path('ad/create', views.AdCreateView.as_view(success_url=reverse_lazy('ads:ads')), name='ad_create'),
    path('ad/<int:pk>/update', views.AdUpdateView.as_view(success_url=reverse_lazy('ads:ads')), name='ad_update'),
    path('ad/<int:pk>/delete', views.AdDeleteView.as_view(success_url=reverse_lazy('ads:ads')), name='ad_delete'),
    path('ad/<int:pk>/ad_picture/', views.stream_file, name="ad_picture"),
]
