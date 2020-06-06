from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
# from .views import EndpointViewSet

#from .views import PredictView
#from .views import StopABTestView
from django.conf.urls import url, include

app_name = 'myportfolio'

urlpatterns = [
    #path('myportfolio/', views.index, name='index'),
    path('myportfolio/', views.index, name='myportfolio_index'),
    path('myportfolio/<int:pk>', views.post_detail, name='post_detail')
    #path('endpoints/', include('endpoints.urls')),

]

