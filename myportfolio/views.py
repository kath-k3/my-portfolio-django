
# Create your views here.
# -*- coding: utf-8 -*-
# from __future__ import unicode_literals
#
# from django.views.generic import TemplateView
#
#


from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404

from rest_framework import viewsets
from rest_framework import mixins
from .models import Post

def index(request):
    posts = Post.objects.all()
    return render(request, 'myportfolio/index.html', {'posts': posts})

# def post_list(request):
#     return render(request, 'myportfolio/post_list.html', {})

# def post_list(request):
#     posts = Post.objects.all()
#     return render(request, 'myportfolio/index.html', {'posts': posts})

def post_detail(request, pk):
    post = Post.objects.get(pk=pk)

    context = {
        'post': post,
    }
    return render(request, 'myportfolio/post_detail.html', context)

