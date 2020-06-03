from django.urls import path
from . import views

from django.urls import path
#from .views import api_sentiment_pred
app_name = 'endpoints'

urlpatterns = [
    path('prediction/predict/', views.call_model.as_view()),
    #path('endpoints/predict/', api_sentiment_pred, name='api_sentiment_pred'),
    path('prediction/', views.endpoint_list),
    path('prediction/<int:pk>/', views.endpoint_detail),
]
