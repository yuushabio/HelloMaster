from django.contrib.auth import authenticate,login
from django.shortcuts import render,redirect
from django.views.generic import View
#from .forms import UserForm
from django.http import HttpResponse
from .models import Item,User
from django.template import loader
from rest_framework import viewsets
from .Serializers import ItemSerializer,UserCreateSerializer
#from django.contrib.auth import get_user_model
from rest_framework.generics import CreateAPIView
#from .models import User
#from .models import Ads


# Create your views here.
class Itemviewset(viewsets.ModelViewSet):
    queryset=Item.objects.all()
    serializer_class=ItemSerializer

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

class UserCreateAPIView(CreateAPIView):
    #User = get_user_model()
    serializer_class = UserCreateSerializer
    queryset = User.objects.all()

'''
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
    form_class=UserForm
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
        return render(request, self.template_name, {'form': form})

'''
