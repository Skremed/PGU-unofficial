from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class LoginTemplateView(TemplateView):
    template_name = 'login/login.html'