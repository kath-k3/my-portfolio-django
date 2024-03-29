"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path

"""

from django.contrib import admin
from django.urls import path, include
from . import views

from django.conf import settings
from django.conf.urls.static import static

from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    #path('', include('myportfolio.urls')),
    path('myportfolio/', include('myportfolio.urls')),
    path('predictor/', include('endpoints.urls')),
    path('projects/', include('projects.urls'))
    #path('model/', views.call_model.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) +\
              static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


# from django.urls import path
# from django.conf import settings
# from django.conf.urls import url
# from django.conf.urls.static import static
# from django.contrib import admin
#
# #from .views import HomeView
#
#
# # urlpatterns = [
# #     url(r'^admin/', admin.site.urls),
# #     url(r'^$', HomeView.as_view(), name='home'),
# # ]
#
# from django.contrib import admin
# from django.urls import include, path
#
# urlpatterns = [
#     path('myportfolio/', include('myportfolio.urls')),
#     path('admin/', admin.site.urls),
# ]
#
#
# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
