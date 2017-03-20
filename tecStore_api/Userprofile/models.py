from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.urlresolvers import reverse

class User(User):
    phone = models.CharField(max_length=15)
    location = models.CharField(max_length=80)

class Item(models.Model):
    #multiple ads can belong to the one user
    #store_id = models.ForeignKey(User, unique=True)
    #store_id=models.ForeignKey(User,on_delete=models.CASCADE())
    item_name=models.CharField(max_length=100)
    price=models.FloatField()
    category=models.CharField(max_length=100,null=True)
    location = models.CharField(max_length=100)
    description=models.TextField()
    first_img = models.ImageField(upload_to='Images/', default='Images/no-img.png',null=True)  # set default if any default='Images/default_image.jpg
    second_img = models.ImageField(upload_to='Images/',default='Images/no-img.png', null=True)
    third_img = models.ImageField(upload_to='Images/',default='Images/no-img.png', null=True)
#class adImages(models.Model):
 #   img_id=models.ForeignKey(Ads,on_delete=models.CASCADE())
    #first_img=models.FileField(null=True)
    #second_img=models.FileField(null=True)
    #third_img=models.FileField(null=True)
    #add date created
    def __str__(self):
        return str(self.id) + '-' + self.item_name+'-' + str(self.price)
