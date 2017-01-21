from django.conf.urls import  url
from simple_gui import views
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm

urlpatterns = [url(r'^myimages/(?P<group_id>[0-9]+)/$', views.MyImages.as_view(), name='myimages'),
url(r'^myimages/$', views.AllMyImages.as_view(), name='myima'),  
url(r'^apimyimages/$', views.APImyImages.as_view(), name='myimago'),   
url(r'^$', views.MyGroups.as_view(), name='usergroups'),]

urlpatterns += [url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^admin/', admin.site.urls),
    url('^register/', CreateView.as_view(template_name='registration/signup.html',
            form_class=UserCreationForm,
            success_url='/simplegui/')),]

