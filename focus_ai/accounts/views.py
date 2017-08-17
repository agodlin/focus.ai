from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import JsonResponse

class LoginPage(TemplateView):
	template_name = 'accounts/login.html'

# Create your views here.


