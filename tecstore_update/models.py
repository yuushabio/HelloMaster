from django.db import models
from django.contrib.auth.models import User
#from django.core.urlresolvers import reverse
'''
class User(User):
    phone_number = models.CharField(max_length=10)

# Create your models here.
class User(models.Model):
    store_id = models.IntegerField()  # each user gets one store id to use for all ads
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    username=models.CharField(max_length=50)
    phone_number=models.CharField(max_length=15)
    email=models.CharField(email,max_length=100) #take email of user
    user_image=models.FileField()
    password=models.CharField() #run encryption on password before storing in db
    status=models.BooleanField(dafault=false) #activation status, check if user is active or not

class Store(models.Model):
    #user = models.ForeignKey(User, on_delete=models.CASCADE,default=1)
    store_name = models.CharField(max_length=100,default='tecStore')
    #img = models.ImageField(upload_to='Images/store', default='Images/no-img.png')
'''


class Item(models.Model):
    #multiple ads can belong to the one user
    #store_id = models.ForeignKey(User,default=1)
    user=models.ForeignKey(User,on_delete=models.CASCADE, default=1)
    item_name=models.CharField(max_length=100)
    price=models.FloatField()
    category=models.CharField(max_length=100,null=True)
    location = models.CharField(max_length=100)
    description=models.TextField()
    first_img = models.ImageField(upload_to='Images/', default='Images/None/no-img.png')  # set default if any default='Images/default_image.jpg
    second_img = models.ImageField(upload_to='Images/',default='Images/None/no-img.png')
    third_img = models.ImageField(upload_to='Images/',default='Images/None/no-img.png')
#class adImages(models.Model):
 #   img_id=models.ForeignKey(Ads,on_delete=models.CASCADE())
    #first_img=models.FileField(null=True)
    #second_img=models.FileField(null=True)
    #third_img=models.FileField(null=True)
    #add date created
    def __str__(self):
        return str(self.id) + '-' + self.item_name+'-' + str(self.price)

#class image(models.Model):
    #img_id=models.ForeignKey(Item,unique=True)
   # first_img = models.ImageField(upload_to='Images/',null=True)#set default if any default='Images/default_image.jpg
   # second_img = models.ImageField(upload_to='Images/',null=True)
   # third_img = models.ImageField(upload_to='Images/',null=True)
