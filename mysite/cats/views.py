from django.shortcuts import render
from django.views.generic import ListView, View
from django.views.generic.edit  import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Cat, Breed

# Create your views here.

# READ
class CatList(LoginRequiredMixin, View):
    template_name = "cats/cat_list.html"
    def get(self, request):
        breed_count = Breed.objects.all().count()
        cat_list = Cat.objects.all()
        ctx = { "cat_list": cat_list, "breed_count": breed_count }
        return render(request, self.template_name , ctx)

class BreedList(LoginRequiredMixin, ListView):
    model = Breed
    template_name = "cats/breed_list.html"

# CREATE
class CatCreate(LoginRequiredMixin, CreateView):
    model = Cat
    fields = "__all__"
    success_url = reverse_lazy("cats:cats")

class BreedCreate(LoginRequiredMixin, CreateView):
    model = Breed
    fields = "__all__"
    success_url = reverse_lazy("cats:cats")

# UPDATE
class CatUpdate(LoginRequiredMixin, UpdateView):
    model = Cat
    fields = "__all__"
    success_url = reverse_lazy("cats:cats")

class BreedUpdate(LoginRequiredMixin, UpdateView):
    model = Breed
    fields = "__all__"
    success_url = reverse_lazy("cats:breed_list")

# DELETE
class CatDelete(LoginRequiredMixin, DeleteView):
    model = Cat
    fields = "__all__"
    success_url = reverse_lazy("cats:cats")

class BreedDelete(LoginRequiredMixin, DeleteView):
    model = Breed
    fields = "__all__"
    success_url = reverse_lazy("cats:breed_list")
