from django.shortcuts import render
from django.views.generic import ListView
#from django.views.generic.edit  import CreateView, UpdateView, DeleteView
#from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Ad
# Create your views here.

class AdListView(ListView):
    model = Ad
