from django.conf.urls import  url
from rest_framework.authtoken import views as tokenview
from rest_framework.urlpatterns import format_suffix_patterns
from uusapp import views
from django.conf.urls import include
from django.contrib.auth.decorators import login_required
from django.views.static import serve
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^images/$', views.ImgList.as_view()), # Responsible for adding images . BasicAUTH 
    url(r'^addimage/$', views.AddImage.as_view()),
    url(r'^images/(?P<pk>[0-9]+)/$', views.show_image),   
    url(r'^getimage/$', views.RetrieveImagesSecure.as_view()),
    url(r'^getimageurl/$', views.RetrieveImages.as_view()),
    url(r'^register/$', views.CreateUserView.as_view()),
    url(r'^groupimages/$', views.GroupList.as_view()),
    url(r'^usergroups/$', views.UserGroups.as_view()),
    url(r'^fileupload/$', views.AddImageNoToken.as_view()),
 
]



urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]