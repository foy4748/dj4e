from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit  import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Auto, Make

# Create your views here.

# READ
class AutoView(LoginRequiredMixin, ListView):
    template_name = "autos/auto_list.html"
    def get(self, request):
        auto_list = Auto.objects.all()
        make_list = Make.objects.all()
        ctx = { "auto_list": auto_list, "make_list": make_list}
        return render(request, self.template_name, ctx)

class MakeView(LoginRequiredMixin, ListView):
    model = Make
    template_name = "autos/make_list.html"

# CREATE
class AutoCreateView(LoginRequiredMixin, CreateView):
    model = Auto
    template_name = "autos/auto_form.html" 
    fields = "__all__"
    success_url = reverse_lazy('autos:autos')

class MakeCreateView(LoginRequiredMixin, CreateView):
    model = Make
    template_name = "autos/make_form.html"
    fields = "__all__"
    success_url = reverse_lazy('autos:autos')


# DELETE
class AutoDeleteView(LoginRequiredMixin, DeleteView):
    model = Auto
    template_name = "autos/auto_confirm_delete.html"
    fields = "__all__"
    success_url = reverse_lazy('autos:autos')

class MakeDeleteView(LoginRequiredMixin, DeleteView):
    model = Make
    template_name = "autos/make_confirm_delete.html"
    fields = "__all__"
    success_url = reverse_lazy('autos:autos')

# EDIT
class AutoUpdateView(LoginRequiredMixin, UpdateView):
    model = Auto
    #template_name = "autos/auto_confirm_delete.html"
    fields = "__all__"
    success_url = reverse_lazy('autos:autos')

class MakeUpdateView(LoginRequiredMixin, UpdateView):
    model = Make
    #template_name = "autos/make_confirm_delete.html"
    fields = "__all__"
    success_url = reverse_lazy('autos:autos')
