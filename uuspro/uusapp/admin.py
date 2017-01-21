from django.contrib import admin
from .models import Img, Eventgroup
from django.contrib.auth.models import User


# Register your models here.



admin.site.register(Img)
admin.site.register(Eventgroup)