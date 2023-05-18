from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit  import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Cat, Breed

# Create your views here.

# READ
class CatList(LoginRequiredMixin, ListView):
    model = Cat
    template_name = "cats/cats_list.html"

# CREATE

# UPDATE

# DELETE
