from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
# from .views import EndpointViewSet


from django.conf.urls import url, include

app_name = 'myportfolio'

urlpatterns = [
    #path('myportfolio/', views.index, name='index'),
    path('', views.index, name='index'),
    path('<int:pk>', views.post_detail, name='post_detail'),
    #path('endpoints/', include('endpoints.urls')),
]
