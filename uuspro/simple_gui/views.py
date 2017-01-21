from django.http.response import HttpResponse
from django.views.generic.list import ListView
from uusapp.models import Img, Eventgroup
from uuspro import settings
from django.contrib.auth.decorators import login_required
from rest_framework.permissions import IsAuthenticated
from django.utils.decorators import method_decorator
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
import requests
from django.views.generic.base import View
from django.core.serializers import json






@method_decorator(login_required, name='dispatch')
class AllMyImages (ListView):
    model = Img
    template_name = 'simple_gui/img_list.html'
    # TODO - override variables view
    media_directory = settings.MEDIA_URL

@method_decorator(login_required, name='dispatch')
class MyImages (AllMyImages):
    def get_queryset(self):
        group_id = self.kwargs['group_id']
        return Img.objects.filter(group=group_id)

class APImyImages (View):
    def get(self, request):
        response = requests.get('http://127.0.0.1:8000/uusapp/images')

        return HttpResponse(response)



    





@method_decorator(login_required, name='dispatch')
class MyGroups (ListView):
    model = Eventgroup
    template_name = 'simple_gui/group_list.html'
    permission_classes = (IsAuthenticated,)
    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        user = self.request.user
        return Eventgroup.objects.filter(owner=user)

