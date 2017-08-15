from django.views.generic import TemplateView
from django.http import JsonResponse

class HomePage(TemplateView):
	template_name = 'home.html'


def post_user_data(request):
        accessToken = request.GET.get('accessToken', None)
        user_id = request.GET.get('userID', None)
        print('Got from frontend', accessToken, user_id)
        data = {}
        return JsonResponse(data)


def post_username(request):
        name = request.GET.get('name', None)
        print('Got from frontend', name)
        data = {}
        return JsonResponse(data)
