from rest_framework import serializers #download dependencies
from .models import Item
from django.contrib.auth import get_user_model
from django.db.models import Q
from rest_framework.serializers import CharField,EmailField,ValidationError
#from .models import image

class ItemSerializer(serializers.ModelSerializer):
    first_img = serializers.ImageField(max_length=None, use_url=True)
    second_img = serializers.ImageField(max_length=None, use_url=True)
    third_img = serializers.ImageField(max_length=None, use_url=True)
    class Meta:
        model = Item
        fields = ('id', 'item_name', 'price', 'category', 'description','first_img','second_img','third_img')
'''
class shoeSerializer(serializers.ModelSerializer):
    first_img = serializers.ImageField(max_length=None, use_url=True)
    second_img = serializers.ImageField(max_length=None, use_url=True)
    third_img = serializers.ImageField(max_length=None, use_url=True)
    class Meta:
        model = Item
        fields = ('id', 'item_name', 'price', 'category', 'description','first_img','second_img','third_img')

class bagSerializer(serializers.ModelSerializer):
    first_img = serializers.ImageField(max_length=None, use_url=True)
    second_img = serializers.ImageField(max_length=None, use_url=True)
    third_img = serializers.ImageField(max_length=None, use_url=True)
    class Meta:
        model = Item
        fields = ('id', 'item_name', 'price', 'category', 'description','first_img','second_img','third_img')



class imageSerializer(serializers.ModelSerializer):
    first_img = serializers.ImageField(max_length=None, use_url=True)
    second_img = serializers.ImageField(max_length=None, use_url=True)
    third_img = serializers.ImageField(max_length=None, use_url=True)

    class Meta:
        model = image
        fields = ('img_id')'''

User = get_user_model()

#login serializer
class UserLoginSerializer(serializers.ModelSerializer):
    token=CharField(allow_blank=True,read_only=True)
    username=CharField(required=False,allow_blank=True)
    email=EmailField(label="Email address",required=False,allow_blank=True)

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
            'token',
        ]

    extra_kwargs = {"password":
                        {"write_only": True}
                    }
    def validate(self, data):
        user_obj=None
        username=data.get('username',None)
        email=data.get('email',None)
        password=data["password"]
        if not email and not username:
            raise ValidationError("A username or email is required")
        user = User.objects.filter(
            Q(email=email)|
            Q(username=username)
        ).distinct()
        user=user.exclude(email__isnull=True).exclude(email__iexact='')
        if user.exists() and user.count()==1:
            user_obj=user.first()#may change
        else:
            raise ValidationError("either the username or email does not exist")
        if user_obj:
            if not user_obj.check_password(password):
                raise ValidationError("Incorrect credentials")
        #data['token']='random token generated for user'
        data['token']="random token"
        return data