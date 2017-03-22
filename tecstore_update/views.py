from django.contrib.auth import authenticate,login
from django.shortcuts import render,redirect
from django.views.generic import View
from .forms import Userform
from django.http import HttpResponse
from .models import Item
from django.template import loader
from rest_framework import viewsets
from .Serializers import ItemSerializer,UserLoginSerializer
#s,shoeSerializer,electSerializer,clothSerializer,otherSerializer,accesSerializer)
#from .models import User
#from .models import Ads
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK,HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from django.db.models import Q

# Create your views here.
class Itemviewset(viewsets.ModelViewSet):
    queryset=Item.objects.all()
    serializer_class=ItemSerializer

class electCategoryviewset(viewsets.ModelViewSet):
    queryset=Item.objects.filter(
            Q(category='electronics')
    )
    serializer_class=ItemSerializer

class clothCategoryviewset(viewsets.ModelViewSet):
    queryset=Item.objects.filter(
            Q(category='clothing')
    )
    serializer_class=ItemSerializer

class otherCategoryviewset(viewsets.ModelViewSet):
    queryset=Item.objects.filter(
            Q(category='others')
    )
    serializer_class=ItemSerializer

class accessCategoryviewset(viewsets.ModelViewSet):
    queryset=Item.objects.filter(
            Q(category='accessories')
    )
    serializer_class=ItemSerializer

'''
def index(request):
    all_items=Item.objects.all()
    template=loader.get_template('Userprofile/index.html')
    context={'all_items':all_items}
    #html=''
    #for item in all_items:
      #  url='/tecStore/'+str(item.id)+'/'
     #   html+='<a href="'+url+'">'+item.item_name+'</a>'
    # get data from db
    #userdata = User.objects.all()
    #advert_data = Ads.objects.all()
    #context = {'userdata': userdata},'advert_data': advert_data}
    # create context
    #return render(request, 'Userprofile/index.html', context)
    return HttpResponse(template.render(context,request))

#detail view
def detail(request,item_id):
    return HttpResponse("<h2> Details for store id:"+str(item_id)+"</h2)")

#request advert using showAd
def showAd(request,store_id):
    try:
        advert=Ads.objects.get(pk=store_id)
    except advert.DoesNotExist():
        raise Http404("this ad does not exist")
    #return the showAd template
    return render(request,'Userprofile/',context)


#create view to handle user registrarion
#inherit from view
class UserFormView(View):
    form_class=Userform
    template_name='Userprofile/registration_form.html'

    #this get function requests form and displays it to user
    def get(self,request):
        form=self.form_class(None)#pass none since get does not retrieve data
        return render(request,self.template_name,{'form':form})

    #post handles submission of data
    def post(self,request):
        form=self.form_class(request.POST)
        #validate form
        if form.is_valid():
            #information is taken but not saved yet
            user=form.save(commit=False)
            #clean data before it is stored in database
            username=form.cleaned_data['username']
            email=form.cleaned_data['email']
            password=form.cleaned_data['password']
            #set_password gets password provided and sets it in database
            user.set_password(password)
            user.save()


            #return user object if found in databse
            user=authenticate(username=username,password=password)
            if user is not None:
                #if user object is returned, user exists
                if user.is_active():
                    #if user is active, login and redirect
                    #pass user object through login function
                    login(request, user)
                    #redirect user to dashboard
                    redirect('Userprofile:index')


        #if form is not correct, send form back to user for refill
        return render(request, self.template_name, {'form': form})'''

class UserLoginAPIView(APIView):
    permission_classes = [AllowAny]
    serializer_class = UserLoginSerializer


    def post(self,request,*args,**kwargs):
        data=request.data
        serializer = UserLoginSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            new_data=serializer.data
            return Response(new_data,HTTP_200_OK)
        return Response(serializer.errors,status=HTTP_400_BAD_REQUEST)