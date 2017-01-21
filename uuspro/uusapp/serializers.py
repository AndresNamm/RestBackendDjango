from rest_framework import serializers
from uusapp.models import Img, Eventgroup
from django.contrib.auth.models import User
from rest_framework import permissions
from django.contrib.auth import get_user_model





class UserSerializer(serializers.ModelSerializer):
    ## password = serailizers.CharField(write_only=True)
    images  = serializers.PrimaryKeyRelatedField(many=True, queryset=Img.objects.all())
    class Meta:
        model = User
        fields = ('id', 'username','password', 'images')
        write_only_fields = ('password',)



class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    #images  = serializers.PrimaryKeyRelatedField(many=True, queryset=Img.objects.all())
    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

        
    class Meta:
        model = User
        fields = ('username','password')
       

class ImgSerializer(serializers.ModelSerializer):

    owner = serializers.ReadOnlyField(source='owner.username')
    image = serializers.ImageField(max_length=None, use_url=True)
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    class Meta:
        model = Img
        fields = ( 'id','title', 'image','owner', 'created', 'group')

class GroupSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Eventgroup
        fields = ( 'id','title','start_time', 'duration', 'owner')      
