from django.shortcuts import render


# -*- coding: utf-8 -*-
# from __future__ import unicode_literals
#
# from django.views.generic import TemplateView
#
#
#
#Below the medium example

from django.shortcuts import render

from django.shortcuts import render, get_object_or_404
from .models import MLAlgorithm
from .serializers import MLAlgorithmSerializer

from .models import MLRequest
from .serializers import MLRequestSerializer

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import viewsets
from rest_framework import mixins

from .models import MLAlgorithmStatus
from .serializers import MLAlgorithmStatusSerializer

from .models import Endpoint
from .serializers import EndpointSerializer

from django.apps import AppConfig
#from django.conf import settings
import os
import pickle
class PredictorConfig(AppConfig):
    # create path to models
    from sklearn.externals import joblib
    CURRENT_DIR = os.path.dirname(__file__)
    model_file = os.path.join(CURRENT_DIR, 'model.file_3')
    model = joblib.load(model_file)
    # load models into separate variables
    # these will be accessible via this class
    # with open(path, 'rb') as pickled:
    #    data = pickle.load(pickled)
    from sklearn.externals import joblib
    model = joblib.load(model_file)
    regressor = model['clf']
    vectorizer = model['vect']

from rest_framework.views import APIView
class call_model(APIView):
    def get(self,request):
        if request.method == 'GET':
            # get sound from request
            sound = request.GET.get('comment')
            print(sound)

            # vectorize sound
            vector = PredictorConfig.vectorizer.transform([sound])
            # predict based on vector
            prediction = PredictorConfig.regressor.predict(vector)[0]
            print(prediction)
            # build response


            if prediction == 0:
                pred_text = 'Not offensive'
            else:
                pred_text = 'Offensive'

            response = {sound: pred_text}
            print(response)
            # return response
            return JsonResponse(response, safe=False)

#another one until here






class EndpointViewSet(
    mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet
):
    serializer_class = EndpointSerializer
    queryset = Endpoint.objects.all()


class MLAlgorithmViewSet(
    mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet
):
    serializer_class = MLAlgorithmSerializer
    queryset = MLAlgorithm.objects.all()


@csrf_exempt
def endpoint_detail(request, pk):
    """
    Retrieve, update or delete a code endpoint.
    """
    try:
        endpoint = Endpoint.objects.get(pk=pk)
    except Endpoint.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = EndpointSerializer(endpoint)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = EndpointSerializer(endpoint, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        endpoint.delete()
        return HttpResponse(status=204)



@csrf_exempt
def endpoint_list(request):
    """
    List all code endpoints, or create a new endpoint.
    """
    if request.method == 'GET':
        endpoints = Endpoint.objects.all()
        serializer = EndpointSerializer(endpoints, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = EndpointSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)




