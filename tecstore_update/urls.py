from django.conf.urls import url
from . import views
from rest_framework import routers
from Userprofile.views import Itemviewset
#from django.views.generic import View

#router=routers.DefaultRouter()
#router.register(r'item',Itemviewset)

urlpatterns = [
   # url(r'^$',views.index,name='index'),
    #url(r'^', include(router.urls)),
    #url(r'^(?P<item_id>[0-9]+)$',views.detail,name='details')

#create user registration view, links to UserFormView created in views
    #url(r'^register/$',views.UserFormView.as_view(),name='register'),
]