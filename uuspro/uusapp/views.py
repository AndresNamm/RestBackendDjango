from django.http import HttpResponse
from uusapp.models import Img, Eventgroup
from uusapp.serializers import ImgSerializer 
from rest_framework import generics
from django.contrib.auth.models import User
from uusapp.serializers import UserSerializer, UserCreateSerializer, GroupSerializer
from rest_framework import permissions
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework import permissions
from uusapp.permissions import IsOwnerOrReadOnly
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.views.static import serve
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
# FOR TOKENS http://fdfdev.com/?p=946
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import redirect
from django.template.loader import get_template

def index(request):
    return HttpResponse("You're at the uusapp index.")

class ImgList (generics.ListCreateAPIView): 
    #authentication_classes = (TokenAuthentication,)
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,
    #IsOwnerOrReadOnly )
    queryset = Img.objects.all()
    serializer_class = ImgSerializer
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class AddImage (generics.CreateAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    #queryset = Img.objects.all()
    serializer_class = ImgSerializer
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class AddImageNoToken (generics.CreateAPIView):
    #authentication_classes = (TokenAuthentication,)
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    #queryset = Img.objects.all()
    serializer_class = ImgSerializer


class CreateUserView (generics.CreateAPIView):
    model = User
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserCreateSerializer


class RetrieveImages (APIView):
    """
    List all snippets, or create a new snippet.
    """
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    
    def get(self, request, format=None):
        #return HttpResponse(2)
        #return HttpResponse( "kasutaja " + request.user.username)
        i_id = self.request.query_params.get('id', None)
        picture = Img.objects.get(id=i_id)
        path = picture.image.path
        return HttpResponse(path)        
        #serializer = ImgSerializer(data=request.query_params)
        #m=serializer.is_valid()
        #return HttpResponse(m)
class ListUserImages (generics.ListAPIView): 
    authentication_classes = (TokenAuthentication,)
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,
    #IsOwnerOrReadOnly )
    #queryset = Img.objects.all()
    serializer_class = ImgSerializer
    def get_queryset(self):
        
        owner_id = self.request.user
        return Img.objects.filter(owner=owner_id)



class GroupList (generics.ListAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = ImgSerializer  
    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        id = self.request.query_params.get('id', None)
        return Img.objects.filter(group=id)

class UserGroups (generics.ListCreateAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = GroupSerializer  
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)    
    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        user = self.request.user
        return Eventgroup.objects.filter(owner=user)

class RetrieveImagesSecure (APIView):
    """
    Authentication is needed for this methods
    """
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    def get(self, request, format=None):
        #return HttpResponse(2)
        #return HttpResponse( "kasutaja " + request.user.username)
        i_id = self.request.query_params.get('id', None)
        picture = Img.objects.get(id=i_id)
        path = picture.image.name
        return serve(request, path, settings.MEDIA_ROOT, True)        
        #serializer = ImgSerializer(data=request.query_params)
        #m=serializer.is_valid()
        #return HttpResponse()
def protected_serve(request, path, document_root=None, show_indexes=False):
    #return HttpResponse(path + document_root )
    return serve(request, path, document_root, show_indexes)


def show_image(request,pk):  
    return HttpResponse("kasutaja " + request.user.username)
'''
    if request.user.username=="admin":    
        picture=Img.objects.get(id=pk)
        path=picture.image.name
        #return HttpResponse(picture.image.name)
        return serve(request, path, settings.MEDIA_ROOT , True)

'''