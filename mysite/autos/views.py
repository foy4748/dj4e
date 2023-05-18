from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Auto, Make

# Create your views here.
class AutoView(ListView):
    model = Auto
    template_name = "autos/auto_list.html"

class AutoCreateView(CreateView):
    model = Auto
    template_name = "autos/auto_form.html"
    fields = "__all__"
