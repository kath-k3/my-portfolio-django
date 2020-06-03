from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
# from .views import EndpointViewSet
# from .views import MLAlgorithmViewSet
# from .views import MLRequestViewSet
#from .views import PredictView
#from .views import StopABTestView
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
app_name = 'myportfolio'

urlpatterns = [
    #path('myportfolio/', views.index, name='index'),
    path('myportfolio/', views.index, name='myportfolio_index'),
    path('myportfolio/<int:pk>', views.post_detail, name='post_detail')
    #path('endpoints/', include('endpoints.urls')),

]

# router = DefaultRouter(trailing_slash=False)
# router.register(r"endpoints", EndpointViewSet, basename="endpoints")
# router.register(r"mlalgorithms", MLAlgorithmViewSet, basename="mlalgorithms")
# router.register(r"mlalgorithmstatuses", MLAlgorithmStatusViewSet, basename="mlalgorithmstatuses")
# router.register(r"mlrequests", MLRequestViewSet, basename="mlrequests")
# router.register(r"abtests", ABTestViewSet, basename="abtests")

