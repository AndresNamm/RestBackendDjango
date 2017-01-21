"""uuspro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from rest_framework.authtoken import views
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.schemas import get_schema_view

schema_view = get_schema_view(title='Pastebin API')


urlpatterns = [
    url(r'uusapp/',include('uusapp.urls')),
    url(r'simplegui/',include('simple_gui.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^api-token-auth/', views.obtain_auth_token),
    url('^schema/$', schema_view),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)