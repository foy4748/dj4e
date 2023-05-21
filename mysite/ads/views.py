from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.base import View
from django.views.generic import ListView
from .owner import OwnerCreateView, OwnerUpdateView, OwnerDeleteView, OwnerDetailView
#from django.views.generic.edit  import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.http import HttpResponse

from .models import Ad
from .forms import CreateForm
# Create your views here.

class AdListView(ListView):
    model = Ad

# Manually Handling 
#   AdCreateView
#   AdUpdateView
# Since it requires to Validate 
# the Picture properties
# That's why it requires some 
# manual approach

# class AdCreateView(OwnerCreateView):
#     model = Ad
#     fields = ['title', 'price', 'text']

# class AdUpdateView(OwnerUpdateView):
#     model = Ad
#     fields = ['title', 'price', 'text']

class AdCreateView(LoginRequiredMixin, View):
    success_url = reverse_lazy('ads:ads')
    template_name = "ads/ad_form.html"

    def get(self, request, pk=None):
        form = CreateForm()
        ctx = {'form': form}
        return render(request, self.template_name, ctx)

    def post(self, request, pk=None):
        form = CreateForm(request.POST, request.FILES or None)

        if not form.is_valid():
            ctx = {'form': form}
            return render(request, self.template_name, ctx)

        # Add owner to the model before saving
        pic = form.save(commit=False)
        pic.owner = self.request.user
        pic.save()
        return redirect(self.success_url)

class AdUpdateView(LoginRequiredMixin, View):
    success_url = reverse_lazy('ads:ads')
    template_name = "ads/ad_form.html"
    def get(self, request, pk):
        pic = get_object_or_404(Ad, id=pk, owner=self.request.user)
        form = CreateForm(instance=pic)
        ctx = {'form': form}
        return render(request, self.template_name, ctx)

    def post(self, request, pk=None):
        pic = get_object_or_404(Ad, id=pk, owner=self.request.user)
        form = CreateForm(request.POST, request.FILES or None, instance=pic)

        if not form.is_valid():
            ctx = {'form': form}
            return render(request, self.template_name, ctx)

        pic = form.save(commit=False)
        pic.save()

        return redirect(self.success_url)


class AdDeleteView(OwnerDeleteView):
    model = Ad

class AdDetailView(OwnerDetailView):
    model = Ad

def stream_file(request, pk):
    pic = get_object_or_404(Ad, id=pk)
    print(pic)
    response = HttpResponse()
    response['Content-Type'] = pic.content_type
    response['Content-Length'] = len(pic.picture)
    response.write(pic.picture)
    return response
