from django.shortcuts import render
from .models import Updating
from django.urls import reverse

class UpdateModeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith(reverse('admin:index')):
            return self.get_response(request)


        settings = Updating.objects.first()
        if settings and settings.status:
            context = {

                'title':settings.title,
                'description':settings.description

            }
            return render(request, 'updating.html', context)
        return self.get_response(request)