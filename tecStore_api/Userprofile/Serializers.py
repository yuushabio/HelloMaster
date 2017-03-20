from rest_framework import serializers #download dependencies
#from django.contrib.auth.models import User
from .models import Item,User

class ItemSerializer(serializers.ModelSerializer):
    first_img = serializers.ImageField(max_length=None, use_url=True)
    second_img = serializers.ImageField(max_length=None, use_url=True)
    third_img = serializers.ImageField(max_length=None, use_url=True)
    class Meta:
        model = Item
        fields = ('id', 'item_name', 'price', 'category', 'description','first_img','second_img','third_img')

class UserCreateSerializer(serializers.ModelSerializer):

    password2 = serializers.CharField(label="Confirm Password",allow_blank=False,write_only=True)
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
            'password2',
            'phone',
            'location',
        ]

    extra_kwargs = {"password":
                        {"write_only": True}
                    }

    def validate_password2(self,value):
        data  = self.get_initial()
        password1 = data.get("password")
        password2 = value
        if password1 != password2:
            raise serializers.ValidationError("Passwords do not match")



    def validate(self,data):
        email_val = data['email']
        user_qs = User.objects.filter(email=email_val)
        if user_qs.exists():
            raise serializers.ValidationError("Email already exist")
        return data


    def create(self,validated_data):
        username = validated_data['username']
        email = validated_data['email']
        password = validated_data['password']
        phone = validated_data['phone']
        location = validated_data['location']
        user_obj = User(
            username = username,
            email = email,
            phone = phone,
            location = location
        )
        user_obj.set_password(validated_data['password'])
        user_obj.save()

        return user_obj