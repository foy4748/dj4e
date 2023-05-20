from django.shortcuts import render
from django.views.generic import ListView
from .owner import OwnerCreateView, OwnerUpdateView, OwnerDeleteView, OwnerDetailView
#from django.views.generic.edit  import CreateView, UpdateView, DeleteView
#from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Ad
# Create your views here.

class AdListView(ListView):
    model = Ad

class AdCreateView(OwnerCreateView):
    model = Ad
    fields = ['title', 'price', 'text']

class AdUpdateView(OwnerUpdateView):
    model = Ad
    fields = ['title', 'price', 'text']

class AdDeleteView(OwnerDeleteView):
    model = Ad

class AdDetailView(OwnerDetailView):
    model = Ad
