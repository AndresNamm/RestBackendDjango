from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings
from random import randint


# This code is triggered whenever a new user has been created and saved to the database

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

class Img(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, null=True,blank=True, default='')
    image = models.ImageField(upload_to='Images/', default = 'Images/None/No-images.jpg')
    owner = models.ForeignKey('auth.User',null=True,default=1,related_name ='images', on_delete=models.CASCADE)
    group = models.ForeignKey('EventGroup', null=True,default=3,related_name ='group_images' , on_delete=models.CASCADE)
    # related name  http://stackoverflow.com/questions/2642613/what-is-related-name-used-for-in-django
    def __str__(self):
        return self.title
    def save(self, *args, **kwargs):
        """
        Overriding the save function to save storage time
        """
        group_id =  get_group_id(self.created)
        self.group = Eventgroup.objects.get(pk=group_id)
        super(Img, self).save(*args, **kwargs)


class Eventgroup(models.Model):
    title = models.CharField(max_length=100, blank=True, default='')
    start_time  = models.DateTimeField(auto_now_add=True)
    duration = models.IntegerField(default=1)
    owner = models.ForeignKey('auth.User',null=True,related_name ='group', on_delete=models.CASCADE)
    def __str__(self):
        return self.title


 #TODO-IMPLEMENT CORRECT GROUPING FUNCTION
def get_group_id(time):
    #print("jou")
    return randint(1,3)