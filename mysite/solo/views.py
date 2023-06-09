from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views import View
from .forms import MyForm

# Create your views here.

class SoloView(LoginRequiredMixin,View):
    def get(self, request):
        form = MyForm()
        ctx = { "form": form }
        return render(request, "solo_assignment/form.html", ctx)

    def post(self, request):
        form = MyForm(request.POST)
        result = None
        if form.is_valid():
            field1_value = form.cleaned_data['field1']
            field2_value = form.cleaned_data['field2']
            result = '{a} {b}'.format(a=field2_value[::-1], b=field1_value[::-1])
            result = result.title()

        form = MyForm()
        ctx = { "form":form, "result":result }
        return render(request, "solo_assignment/form.html", ctx)

