from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from . import models

class One(APIView):
    def get(self):
        pass

# @api_view(['GET', 'POST']):
# def favorites(request):
#     if request.method == 'GET':


