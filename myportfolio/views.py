from django.shortcuts import render

# Create your views here.
# -*- coding: utf-8 -*-
# from __future__ import unicode_literals
#
# from django.views.generic import TemplateView
#
#
# class HomeView(TemplateView):
#     template_name = "home.html"
#
#     def get_context_data(self, **kwargs):
#         context = super(HomeView, self).get_context_data(**kwargs)
#         return context


from django.http import HttpResponse

def index(request):
    return HttpResponse("This is my index page")
