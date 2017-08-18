from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import JsonResponse

class LoginPage(TemplateView):
	template_name = 'accounts/login.html'

class ILoginPage(TemplateView):
	template_name = 'accounts/ig_login.html'        

# Create your views here.


