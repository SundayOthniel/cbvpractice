from django.shortcuts import render
from django.views.generic import ListView
from .models import CbvModel


class list_view(ListView):
    model = CbvModel
    template_name = 'index.html'