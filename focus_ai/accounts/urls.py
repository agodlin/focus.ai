from django.conf.urls import url
from . import views


app_name = 'accounts'

urlpatterns = [
    url(r'fb-login/$', views.LoginPage.as_view(), name='fb-login'),
    url(r'ig-login/$', views.ILoginPage.as_view(), name='ig-login'),
    ]
